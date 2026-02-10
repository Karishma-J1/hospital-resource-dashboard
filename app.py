from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hospital Resource Utilization Dashboard Backend is Running"

if __name__ == "__main__":
    # Get port from Render environment (very important)
    port = int(os.environ.get("PORT", 5000))
    
    # Run on 0.0.0.0 so Render can detect it
    app.run(host="0.0.0.0", port=port)
