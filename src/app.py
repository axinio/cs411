import requests
from flask import Flask, render_template
from flask import request

new_list = []

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clear", methods=['POST'])
def clear():
    new_list.clear()
    return "Success", 200

@app.route("/test", methods=['POST'])
def process():
    data = request.get_json()
    if "id" in data:
        print(data["id"])
        addMain(data["id"])
        new_d = adverse()
        if new_d != None:
            new_d = new_d.json()
        print(new_d)
    return "Success", 200

def addMain(medNum):
    if len(new_list) == 0:
        new_list.append(medNum)
    elif medNum not in new_list:
        new_list.append(medNum)

def adverse():
    base_add = 'https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis='
    if len(new_list) > 1:
        for x in range(len(new_list)):
                base_add = base_add + (str(new_list[x])+'+')
        get_resp = requests.get(base_add)
        print(base_add)
    else:
        return None
    return get_resp
