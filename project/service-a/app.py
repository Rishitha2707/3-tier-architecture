from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        res = requests.get("http://service-b:5001/order")
        return f"Service A → {res.text}"
    except:
        return "Service A: Cannot reach Service B"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
