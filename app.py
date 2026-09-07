from flask import Flask, send_file

app = Flask(name)

@app.route("/")
def home():
    return send_file("index.html")

if name == "main":
    app.run(host="0.0.0.0", port=10000)
