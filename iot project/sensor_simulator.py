import time
import random
from Adafruit_IO import Client
from datetime import datetime

# ── Adafruit IO Credentials ──────────────────────────────────────────
ADAFRUIT_IO_USERNAME = "suraj09871"
ADAFRUIT_IO_KEY      = "aio_vQQJ63VcvX79VdT1xcQdhQYz4H2v"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# ── Send Sensor Data ─────────────────────────────────────────────────
def send_sensor_data():
    temperature = round(random.uniform(20, 40), 1)
    humidity    = round(random.uniform(40, 80), 1)
    gas         = random.randint(0, 1)
    motion      = random.randint(0, 1)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'='*45}")
    print(f"  NEXUS WAREHOUSE — AUTO SENSOR UPDATE")
    print(f"  Time       : {now}")
    print(f"{'='*45}")

    try:
        aio.send_data("temperature", temperature)
        print(f"  ✓ Temperature : {temperature} °C")
    except Exception as e:
        print(f"  ✗ Temperature failed: {e}")

    try:
        aio.send_data("humidity", humidity)
        print(f"  ✓ Humidity    : {humidity} %")
    except Exception as e:
        print(f"  ✗ Humidity failed: {e}")

    try:
        aio.send_data("gas", gas)
        status = "ALERT ⚠" if gas == 1 else "CLEAR ✓"
        print(f"  ✓ Gas         : {gas}  ({status})")
    except Exception as e:
        print(f"  ✗ Gas failed: {e}")

    try:
        aio.send_data("motion", motion)
        status = "DETECTED ◉" if motion == 1 else "NONE ●"
        print(f"  ✓ Motion      : {motion}  ({status})")
    except Exception as e:
        print(f"  ✗ Motion failed: {e}")

    print(f"{'='*45}")
    print(f"  Next update in 15 minutes...")
    print(f"{'='*45}\n")

# ── Main Loop ────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n  NEXUS Sensor Simulator Started!")
    print("  Sending data to Adafruit IO every 15 minutes.")
    print("  Press Ctrl+C to stop.\n")

    while True:
        send_sensor_data()
        time.sleep(15 * 60)   # 15 minutes