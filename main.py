from flask import Flask
import pymongo
import json

client = pymongo.MongoClient("mongodb://192.168.1.107:27017")
db = client["mytestdb"]
collection = db["users"]

app = Flask(__name__)

##################################
@app.route('/')
def hello():
    return 'Hello, World!'


##################################
@app.route('/write/<name>')
def write(name):
    res = collection.insert_one({"name": name})
    if res.acknowledged:
        return "Saved %s" % name
    else:
        return "Not saved"



##################################
@app.route('/read')
def read():
    items = []
    for doc in collection.find({}, {"_id": 0}):
        items.append(doc)
    
    return json.dumps(items)


##################################
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
