from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Alice 👋"

@app.route("/pod")
def pod():
    pod_name = os.environ.get("POD_NAME") or os.uname().nodename
    return f"Hello from pod: {pod_name}\n"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
