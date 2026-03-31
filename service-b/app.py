from flask import Flask
import requests

app = Flask(__name__)

@app.route("/order")
def order():
    try:
        res = requests.get("http://service-c:5002/inventory")
        return f"Order Service → {res.text}"
    except:
        return "Order Service: Cannot reach Inventory"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
