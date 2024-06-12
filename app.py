from flask import Flask, request, render_template
import pickle, os

def validasi_inputan(form_data):
    errors = {}
    if not form_data.get("Age"):
        errors["Age"] = "Umur tidak boleh kosong."
    if not form_data.get("SystolicBP"):
        errors["SystolicBP"] = "Tekanan darah tinggi tidak boleh kosong."
    if not form_data.get("DiastolicBP"):
        errors["DiastolicBP"] = "Tekanan darah rendah tidak boleh kosong."
    if not form_data.get("BS"):
        errors["BS"] = "Level gula darah tidak boleh kosong."
    if not form_data.get("BodyTemp"):
        errors["BodyTemp"] = "Suhu tubuh tidak boleh kosong."
    if not form_data.get("HeartRate"):
        errors["HeartRate"] = "Detak Jantung tidak boleh kosong."
    return errors

def validate_data(record):
    errors = {}
    if record["Age"] <= 10 or record["Age"] >= 70:
        errors["Age"] = "Umur harus diantara 10 dan 70 tahun"

    if record["SystolicBP"] <= 70 or record["SystolicBP"] >= 160:
        errors["SystolicBP"] = "Tekanan darah tinggi harus diantara 70 dan 160 mmHg."

    if record["DiastolicBP"] <= 49 or record["DiastolicBP"] >= 100:
        errors["DiastolicBP"] = "Tekanan darah rendah harus diantara 49 dan 100 mmHg."

    if record["SystolicBP"] <= record["DiastolicBP"]:
        errors["BP"] = "Tekanan darah tinggi harus lebih tinggi dari tekanan darah rendah."

    if record["BS"] <= 6.0 or record["BS"] >= 19.0:
        errors["BS"] = "Level gula darah harus diantara 6.0 dan 19.0 mmol/L."

    if record["BodyTemp"] <= 90 or record["BodyTemp"] >= 110:
        errors["BodyTemp"] = "Suhu tubuh harus diantara 90 dan 110 derajat fahrenheit."

    if record["HeartRate"] <= 60 or record["HeartRate"] >= 90:
        errors["HeartRate"] = "Detak Jantung harus diantara 60 dan 90 bpm."

    return errors

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
        # Validasi inputan tidak boleh kosong
        errors = validasi_inputan(request.form)
        if not errors:
            record = {
                "Age": int(request.form.get("Age")),
                "SystolicBP": int(request.form.get("SystolicBP")),
                "DiastolicBP": int(request.form.get("DiastolicBP")),
                "BS": float(request.form.get("BS")),
                "BodyTemp": float(request.form.get("BodyTemp")),
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
                risk = classifier_load.predict([input_data])

    return render_template('index.html', risk=risk, errors=errors, record=request.form)

if __name__ == "__main__":
    app.run()
