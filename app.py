from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hospital Resource Utilization Dashboard Backend is Running"

if __name__ == "__main__":
    app.run()
