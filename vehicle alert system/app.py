from flask import Flask, render_template, request

app = Flask(__name__)

def detect_faults(data):
    alerts = []

    # Engine Temperature
    if data["engine_temp"] > 110:
        alerts.append(("Engine Overheating", "High"))
    elif data["engine_temp"] > 100:
        alerts.append(("Engine Heating", "Medium"))

    # Fuel Level
    if data["fuel_level"] < 10:
        alerts.append(("Low Fuel", "Medium"))

    # Battery Voltage
    if data["battery_voltage"] < 10:
        alerts.append(("Critical Battery Voltage", "High"))
    elif data["battery_voltage"] < 11:
        alerts.append(("Low Battery Voltage", "Medium"))

    # Brake Status
    if data["brake_status"] == "FAIL":
        alerts.append(("Brake Failure", "High"))

    # RPM
    if data["rpm"] > 6500:
        alerts.append(("High RPM", "Medium"))

    # Oil Pressure
    if data["oil_pressure"] < 20:
        alerts.append(("Low Oil Pressure", "High"))

    return alerts


@app.route("/", methods=["GET", "POST"])
def index():
    alerts = []
    if request.method == "POST":
        data = {
            "engine_temp": float(request.form["engine_temp"]),
            "fuel_level": float(request.form["fuel_level"]),
            "battery_voltage": float(request.form["battery_voltage"]),
            "rpm": float(request.form["rpm"]),
            "oil_pressure": float(request.form["oil_pressure"]),
            "brake_status": request.form["brake_status"]
        }

        alerts = detect_faults(data)

    return render_template("index.html", alerts=alerts)


if __name__ == "__main__":
    app.run(debug=True)