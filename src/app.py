# app.py
from flask import Flask, jsonify

app = Flask(__name__)

def suma(a, b):
    return a + b

@app.route("/")
def index():
    return jsonify({"message": "Hola desde la app de examen", "status": "ok"})

@app.route("/sum/<int:a>/<int:b>")
def sum_route(a, b):
    return jsonify({"result": suma(a, b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
