from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = "diabetes_prediction_secret"

# ===============================
# Load ML Model
# ===============================

model = joblib.load("model/diabetes_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# ===============================
# Login Credentials
# ===============================

USERNAME = "admin"
PASSWORD = "admin123"

# ===============================
# Login Page
# ===============================

@app.route("/")
def login():

    if "user" in session:
        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ===============================
# Login Validation
# ===============================

@app.route("/login", methods=["POST"])
def user_login():

    username = request.form["username"]
    password = request.form["password"]

    if username == USERNAME and password == PASSWORD:

        session["user"] = username

        return redirect(url_for("dashboard"))

    return render_template(
        "login.html",
        error="Invalid Username or Password"
    )


# ===============================
# Dashboard
# ===============================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


# ===============================
# Patient Details
# ===============================

@app.route("/patient")
def patient():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("patient.html")


# ===============================
# Prediction Page
# ===============================

@app.route("/prediction")
def prediction():

    if "user" not in session:
        return redirect(url_for("login"))

    patient = {

        "name": request.args.get("name", ""),

        "age": request.args.get("age", ""),

        "gender": request.args.get("gender", ""),

        "phone": request.args.get("phone", ""),

        "address": request.args.get("address", "")

    }

    return render_template(
        "index.html",
        patient=patient
    )


# ===============================
# Prediction
# ===============================

@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect(url_for("login"))

    # --------------------
    # Patient Details
    # --------------------

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    phone = request.form["phone"]
    address = request.form["address"]

    # --------------------
    # ML Inputs
    # --------------------

    data = [

        float(request.form["Pregnancies"]),

        float(request.form["Glucose"]),

        float(request.form["BloodPressure"]),

        float(request.form["SkinThickness"]),

        float(request.form["Insulin"]),

        float(request.form["BMI"]),

        float(request.form["DPF"]),

        float(request.form["Age"])

    ]

    data = np.array(data).reshape(1, -1)

    data = scaler.transform(data)

    prediction = model.predict(data)

    probability = model.predict_proba(data)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction[0] == 1:

        result = "Patient is Diabetic"

    else:

        result = "Patient is Not Diabetic"

    return render_template(

        "result.html",

        prediction=result,

        confidence=confidence,

        name=name,

        age=age,

        gender=gender,

        phone=phone,

        address=address

    )


# ===============================
# Health Tips
# ===============================

@app.route("/health")
def health():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("health.html")


# ===============================
# About Project
# ===============================

@app.route("/about")
def about():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("about.html")


# ===============================
# Logout
# ===============================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ===============================
# Run App
# ===============================

if __name__ == "__main__":

    app.run(debug=True)