from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config["DEBUG"] = True

key = os.urandom(24).hex()

URL = [{"GITPOD_URL" : "http://www.domain.com/" + key}]

@app.route("/send", methods=["POST", "GET"])
def send():
    return jsonify(URL)

if __name__ == "__main__":
    app.run()