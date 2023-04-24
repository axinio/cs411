import requests
from flask import Flask, render_template, request, jsonify
from reqprocess import addMain, newChecker


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clear", methods=['POST'])
def clear():
    return "Success", 200

@app.route("/test", methods=['GET','POST'])
def process():
    data = request.get_json()
    if "id" in data:
        i = data["id"]
        print(i)
        addMain(i)
        new_d = newChecker()
        if new_d == None:
            return "Success"
        else:
            yes = jsonify(new_d)
        print(new_d)
    return yes, 200

