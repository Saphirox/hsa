#!/usr/bin/env python
import os
from datetime import datetime

from elasticsearch import Elasticsearch
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
mongo_client = MongoClient("mongo:27017")
db = mongo_client["app"]
notes_collection = db['notes']
es_client = Elasticsearch(
    ['http://elasticsearch:9200'],  # Use your Elasticsearch host
    verify_certs=False,
    ssl_show_warn=False  # Optional: suppresses warnings about insecure SSL
)

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        note_content = request.form.get('content')
        if note_content:
            result = notes_collection.insert_one({'content': note_content})
            es_client.index(index="my-index-000001", id=result.inserted_id, body={"content": note_content,
                                                                                  "timestamp": datetime.now()})
        return redirect("/")

    notes = list(notes_collection.find())
    return render_template('index.html', notes=notes)


@app.route('/delete-all', methods=['POST'])
def remove_all_notes():
    mongo_client["app"]["notes"].delete_many({})
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9091), debug=True)
