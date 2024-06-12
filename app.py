from flask import Flask, request, render_template
import pickle, os

def validate_data(record):
    errors = {}
    if record["Age"] < 10 or record["Age"] > 70:
        errors["Age"] = "Umur harus diantara 10 dan 70 tahun"

    if record["SystolicBP"] < 70 or record["SystolicBP"] > 160:
        errors["SystolicBP"] = "Tekanan darah tinggi harus diantara 70 dan 160 mmHg."

    if record["DiastolicBP"] < 49 or record["DiastolicBP"] > 100:
        errors["DiastolicBP"] = "Tekanan darah rendah harus diantara 49 dan 100 mmHg."

    if record["SystolicBP"] <= record["DiastolicBP"]:
        errors["BP"] = "Tekanan darah tinggi harus lebih tinggi dari tekanan darah rendah."

    if record["BS"] < 6.0 or record["BS"] > 19.0:
        errors["BS"] = "Level gula darah harus diantara 6.0 dan 19.0 mmol/L."

    if record["BodyTemp"] < (34 * 9/5 ) + 32 or record["BodyTemp"] > (41 * 9/5 ) + 32:
        errors["BodyTemp"] = "Suhu tubuh harus diantara 34 dan 41 derajat celsius."

    if record["HeartRate"] < 60 or record["HeartRate"] > 90:
        errors["HeartRate"] = "Detak Jantung harus diantara 60 dan 90 bpm."

    return errors

# def convert_risk(pred):
#     if pred == "high risk":
#         return 0
#     elif pred == "low risk":
#         return 1
#     elif pred == "mid risk":
#         return 2

# Load models
classifier_load = pickle.load(open('stacking_classifier_model.sav', 'rb'))


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    risk = None
    errors = {}
    if request.method == "POST":
        record = {
            "Age": int(request.form.get("Age")),
            "SystolicBP": int(request.form.get("SystolicBP")),
            "DiastolicBP": int(request.form.get("DiastolicBP")),
            "BS": float(request.form.get("BS")),
            "BodyTemp": ( float(request.form.get("BodyTemp")) * 9/5 ) + 32,
            "HeartRate": int(request.form.get("HeartRate")),
        }

        errors = validate_data(record)
        if not errors:
            input_data = [
                record["Age"],
                record["SystolicBP"],
                record["DiastolicBP"],
                record["BS"],
                record["BodyTemp"],
                record["HeartRate"],
            ]

            # Membuat prediksi dari model
            risk  = classifier_load.predict([input_data])

    return render_template('index.html', risk=risk, errors=errors, record=request.form)

if __name__ == "__main__":
    app.run()
