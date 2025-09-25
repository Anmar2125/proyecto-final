# src/app.py
from flask import Flask, jsonify
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "project": "Microred con PLC S7-1200 + BMS + ML",
        "status": "running",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/ready')
def ready():
    return jsonify({"status": "ready"})

@app.route('/simulation/status')
def simulation_status():
    # Simular datos de la microrred
    data = {
        "plc_status": "running",
        "bms_soc": 75.5,
        "solar_power": 3.2,
        "load_demand": 2.8,
        "ml_prediction": 3.1
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)