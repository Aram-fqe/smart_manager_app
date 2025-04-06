from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("fan_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hour = int(request.form["hour"])
    day = int(request.form["day"])
    month = int(request.form["month"])
    temperature = float(request.form["temperature"])
    status = int(request.form["status"])
    rpm = int(request.form["rpm"])
    voltage = float(request.form["voltage"])
    current = float(request.form["current"])

    features = [[hour, day, month, temperature, status, rpm, voltage, current]]
    prediction = model.predict(features)[0]
    if prediction > 5:  # threshold for overuse
      alert = "⚠️ High usage detected!"
    elif status == 0 and prediction > 1:
      alert = "⚠️ Device might be left ON without use!"
    else:
      alert = "✅ Usage is normal"

    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/live-data")
def live_data():
    # You can read live data from sensor or simulate it
    import random
    power = round(random.uniform(10, 50), 2)
    return {"power": power}

