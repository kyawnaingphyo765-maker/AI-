from flask import Flask, send_file

app = Flask(_name_)

@app.route("/")
def home():
    return send_file("index.html")

if_name_== "_main_":
    app.run(host="0.0.0.0", port=10000)
