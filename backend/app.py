from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"patients": [], "appointments": []}
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/patients', methods=['GET','POST'])
def patients():
    data = load_data()
    if request.method == 'POST':
        patient = request.json
        data['patients'].append(patient)
        save_data(data)
        return jsonify(patient), 201
    return jsonify(data['patients'])

@app.route('/appointments', methods=['GET','POST'])
def appointments():
    data = load_data()
    if request.method == 'POST':
        appt = request.json
        data['appointments'].append(appt)
        save_data(data)
        return jsonify(appt), 201
    return jsonify(data['appointments'])

if __name__ == '__main__':
    app.run(debug=True)
