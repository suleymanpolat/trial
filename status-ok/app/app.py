
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def status():
    return jsonify(status="OK")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333)