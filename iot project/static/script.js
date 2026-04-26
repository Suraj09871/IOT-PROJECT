Chart.defaults.color = '#8faec8';
Chart.defaults.borderColor = '#1e3a5f';
Chart.defaults.font.family = "'Share Tech Mono', monospace";
Chart.defaults.font.size = 11;

const BLUE = '#0ea5e9';
const CYAN = '#06d6f0';
const GREEN = '#10d980';
const YELLOW = '#f59e0b';
const RED = '#ef4444';
const PURPLE = '#a855f7';

const gridOpts = {
  color: 'rgba(30,58,95,0.5)',
  drawBorder: false,
};

// Chart 1 - Temperature Line
new Chart(document.getElementById("chart1"), {
  type: "line",
  data: {
    labels: ["08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"],
    datasets: [{
      label: "Temperature (°C)",
      data: [24, 27, 31, 33, 30, 28, 26, 25],
      borderColor: BLUE,
      backgroundColor: 'rgba(14,165,233,0.08)',
      fill: true,
      tension: 0.4,
      pointBackgroundColor: BLUE,
      pointRadius: 4,
      pointHoverRadius: 6,
      borderWidth: 2,
    }, {
      label: "Humidity (%)",
      data: [62, 58, 54, 50, 55, 60, 65, 63],
      borderColor: CYAN,
      backgroundColor: 'rgba(6,214,240,0.04)',
      fill: true,
      tension: 0.4,
      pointBackgroundColor: CYAN,
      pointRadius: 4,
      pointHoverRadius: 6,
      borderWidth: 2,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: { position: 'top', labels: { boxWidth: 12, padding: 16 } }
    },
    scales: {
      x: { grid: gridOpts },
      y: { grid: gridOpts, beginAtZero: false }
    }
  }
});

// Chart 2 - Weekly Inventory Bar
new Chart(document.getElementById("chart2"), {
  type: "bar",
  data: {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
    datasets: [{
      label: "Units",
      data: [220, 275, 310, 290, 340],
      backgroundColor: [
        'rgba(14,165,233,0.7)',
        'rgba(14,165,233,0.7)',
        'rgba(6,214,240,0.7)',
        'rgba(14,165,233,0.7)',
        'rgba(6,214,240,0.8)',
      ],
      borderColor: BLUE,
      borderWidth: 1,
      borderRadius: 4,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: { legend: { display: false } },
    scales: {
      x: { grid: { display: false } },
      y: { grid: gridOpts, beginAtZero: true }
    }
  }
});

// Chart 3 - Zone Pie
new Chart(document.getElementById("chart3"), {
  type: "doughnut",
  data: {
    labels: ["Zone A", "Zone B", "Zone C"],
    datasets: [{
      data: [40, 35, 25],
      backgroundColor: [
        'rgba(16,217,128,0.8)',
        'rgba(14,165,233,0.8)',
        'rgba(245,158,11,0.8)',
      ],
      borderColor: '#080c14',
      borderWidth: 3,
      hoverOffset: 6,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    cutout: '65%',
    plugins: {
      legend: { position: 'bottom', labels: { boxWidth: 10, padding: 12 } }
    }
  }
});

// Chart 4 - Storage Donut
new Chart(document.getElementById("chart4"), {
  type: "doughnut",
  data: {
    labels: ["Used", "Available"],
    datasets: [{
      data: [73, 27],
      backgroundColor: [
        'rgba(168,85,247,0.8)',
        'rgba(30,58,95,0.4)',
      ],
      borderColor: '#080c14',
      borderWidth: 3,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    cutout: '70%',
    plugins: {
      legend: { position: 'bottom', labels: { boxWidth: 10, padding: 12 } }
    }
  }
});

// Chart 5 - Shipments Bar
new Chart(document.getElementById("chart5"), {
  type: "bar",
  data: {
    labels: ["Incoming", "Outgoing"],
    datasets: [{
      label: "Shipments",
      data: [35, 20],
      backgroundColor: [
        'rgba(16,217,128,0.75)',
        'rgba(239,68,68,0.75)',
      ],
      borderColor: [GREEN, RED],
      borderWidth: 1,
      borderRadius: 6,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: { legend: { display: false } },
    scales: {
      x: { grid: { display: false } },
      y: { grid: gridOpts, beginAtZero: true }
    }
  }
});
