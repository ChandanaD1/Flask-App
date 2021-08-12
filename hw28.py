# flask app

from flask import Flask, jsonify, request

app = Flask(__name__) 

tasks = [
    {"id":1,
    "title":"brushing teeth",
    "description":"put toothpaste on toothbrush and brush your teeth for 2 min, spit, and rinse",
    "status":False},
    {"id":2,
    "title":"reading book",
    "description":"read book",
    "status":False}
]

@app.route("/post-data",methods=["POST"]) #must specify "post" since "get" is the default
def add_tasks():
    if not request.json:
        return(jsonify({
            "status":"error",
            "message":"please provide the correct data"
        }),400)
    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    tasks.append(task)
    return(jsonify({
        "status":"success",
        "message":"the task was added successfully"
    }))