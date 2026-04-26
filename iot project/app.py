from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
from Adafruit_IO import Client

app = Flask(__name__)

# =============================
# DATABASE CONFIG
# =============================
DB_NAME = "database.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# =============================
# ADAFRUIT IO CONFIG
# =============================
ADAFRUIT_IO_USERNAME = "xxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual username
ADAFRUIT_IO_KEY = "xxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual key

# Example:
# ADAFRUIT_IO_USERNAME = "suraj09871"
# ADAFRUIT_IO_KEY = "aio_xxxxxxxxxxxxxxxxxxxxx"

try:
    aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
except Exception as e:
    print("Adafruit IO connection failed:", e)
    aio = None


# =============================
# DASHBOARD ROUTE
# =============================
@app.route("/")
def dashboard():
    conn = get_connection()
    cur = conn.cursor()

    # Total units
    cur.execute("SELECT COALESCE(SUM(qty), 0) FROM products")
    total_items = cur.fetchone()[0]

    # Total products
    cur.execute("SELECT COUNT(*) FROM products")
    total_products = cur.fetchone()[0]

    conn.close()

    # Simulated sensor values
    temperature = round(random.uniform(20, 40), 1)
    humidity = round(random.uniform(40, 80), 1)
    gas = random.randint(0, 1)
    motion = random.randint(0, 1)

    # Send to Adafruit IO
    if aio:
        try:
            aio.send_data("temperature", temperature)
            aio.send_data("humidity", humidity)
            aio.send_data("gas", gas)
            aio.send_data("motion", motion)
        except Exception as e:
            print("Adafruit IO Error:", e)

    data = {
        "temperature": temperature,
        "humidity": humidity,
        "gas": gas,
        "motion": motion,
        "total_items": total_items,
        "total_products": total_products,
        "incoming": random.randint(10, 40),
        "outgoing": random.randint(5, 30),
    }

    return render_template("dashboard.html", data=data)


# =============================
# INVENTORY PAGE
# =============================
@app.route("/inventory")
def inventory():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM products ORDER BY id DESC")
    products = cur.fetchall()

    conn.close()
    return render_template("inventory.html", products=products)


# =============================
# ADD PRODUCT
# =============================
@app.route("/add", methods=["POST"])
def add_product():
    name = request.form["name"]
    qty = request.form["qty"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products (name, qty) VALUES (?, ?)",
        (name, qty)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("inventory"))


# =============================
# EDIT PRODUCT
# =============================
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        qty = request.form["qty"]

        cur.execute(
            "UPDATE products SET name = ?, qty = ? WHERE id = ?",
            (name, qty, id)
        )

        conn.commit()
        conn.close()
        return redirect(url_for("inventory"))

    cur.execute("SELECT * FROM products WHERE id = ?", (id,))
    product = cur.fetchone()

    conn.close()
    return render_template("edit.html", product=product)


# =============================
# DELETE PRODUCT
# =============================
@app.route("/delete/<int:id>")
def delete_product(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM products WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("inventory"))


# =============================
# REPORT PAGE
# =============================
@app.route("/report")
def report():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM products ORDER BY id DESC")
    products = cur.fetchall()

    conn.close()
    return render_template("report.html", products=products)


# =============================
# RUN APP
# =============================
if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
