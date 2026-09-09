from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return f"""
    <h1>KubeForge</h1>
    <p>Kubernetes-powered application</p>
    <p>Version: {VERSION}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
