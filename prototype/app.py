import requests
from flask import Flask, render_template, request, jsonify, make_response, Response
from flask_cors import CORS,cross_origin
from reqprocess import *
from firedb import *


app = Flask(__name__)
cors = CORS(app)

global current_id_main

current_id_main = None

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/identifier", methods=['POST'])
def indentity_set():
    data = request.data
    print("this is here")
    print(data.decode())
    current_id = current_id_main
    if current_id == None:
        current_id = data.decode()
        global new_ID
        new_ID = current_id
        clear_curr_list()
        print(current_id)
        if userFinder(current_id) == True:
            re_data = retrieveData(current_id)
            original = repopulate_list(re_data)
            return jsonify(original), 200
        else:
            clear_curr_list()
            new_ID = current_id

    else:
        if current_id != data.decode():
            clear_curr_list()
            current_id = data.decode()
            new_ID = current_id
            re_data = retrieveData(current_id)
            original = repopulate_list(re_data)
            return jsonify(original), 200

    return "Success", 200

@app.route("/clear", methods=['POST'])
def clear():
    return "Success", 200

if __name__ == "__main__":
    app.run(debug = True)

@app.route("/test", methods=['GET','POST'])
def process():
    current_id = new_ID
    data = request.get_json()
    processing = request_process_path(current_id,data)
    if processing == None:
        return "Success"
    else:
        yes = jsonify(processing)
    return yes, 200

