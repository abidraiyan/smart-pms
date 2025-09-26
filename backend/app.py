
from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os, uuid, datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"patients": [], "appointments": []}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/register", methods=["POST"])
def register():
    data = load_data()
    body = request.get_json(force=True)
    # basic validation
    required = ["name", "email"]
    for r in required:
        if r not in body or not body[r]:
            return jsonify({"error": f"Missing field: {r}"}), 400
    # simple duplicate check by email
    for p in data["patients"]:
        if p["email"].lower() == body["email"].lower():
            return jsonify({"error": "Email already registered"}), 409
    patient = {
        "id": str(uuid.uuid4())[:8],
        "name": body["name"],
        "email": body["email"],
        "created_at": datetime.datetime.utcnow().isoformat() + "Z"
    }
    data["patients"].append(patient)
    save_data(data)
    return jsonify({"message": "Registered", "patient": patient}), 201

@app.route("/patients", methods=["GET"])
def patients():
    data = load_data()
    return jsonify(data["patients"]), 200

@app.route("/book", methods=["POST"])
def book():
    data = load_data()
    body = request.get_json(force=True)
    required = ["patient_email", "date", "time", "doctor"]
    for r in required:
        if r not in body or not body[r]:
            return jsonify({"error": f"Missing field: {r}"}), 400
    # find patient
    patient = next((p for p in data["patients"] if p["email"].lower() == body["patient_email"].lower()), None)
    if not patient:
        return jsonify({"error": "Patient not found. Register first."}), 404
    appt = {
        "id": str(uuid.uuid4())[:8],
        "patient_email": body["patient_email"],
        "patient_name": patient["name"],
        "date": body["date"],
        "time": body["time"],
        "doctor": body["doctor"],
        "created_at": datetime.datetime.utcnow().isoformat() + "Z"
    }
    data["appointments"].append(appt)
    save_data(data)
    return jsonify({"message": "Appointment booked", "appointment": appt}), 201

@app.route("/appointments", methods=["GET"])
def appointments():
    data = load_data()
    # sort by date/time simple
    return jsonify(sorted(data["appointments"], key=lambda a: (a["date"], a["time"]))), 200

if __name__ == "__main__":
    # Run on 0.0.0.0 so it works if you host later
    app.run(host="0.0.0.0", port=5000, debug=True)
