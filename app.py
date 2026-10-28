
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "CloudReady",
        "message": "My cloud computing project is running!",
        "status": "Healthy",
        "technology": "Python and Flask"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

