# ⚡ Smart Energy Manager

A smart web-based system to monitor and predict energy usage of electronic devices in real-time. Built using Python (Flask), machine learning, and an ESP32 sensor network.

---

## 🔍 Features

- 📊 **Live Monitoring** – Real-time data from devices like CPU fans and DC motors.
- 🔔 **Smart Alerts** – Notifies when devices are overused or left idle.
- 📈 **Energy Forecasting** – Predicts monthly energy consumption & electricity bill.
- 🌐 **Web Interface** – Beautiful dark-mode dashboard built with HTML/CSS/Flask.
- 🔌 **Hardware Integration** – Uses current, voltage, temperature, and RPM sensors via ESP32.

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Dark Mode)
- **ML Model**: Joblib + scikit-learn
- **Hardware**: ESP32, Current/Voltage/Temp Sensors
- **Database**: [Optional if storing data long-term]

---

## 🚀 Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/Aram-fqe/smart_manager_app.git
   cd smart_manager_app

pip install flask numpy joblib
python app.py
http://127.0.0.1:5000
