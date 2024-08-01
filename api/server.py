#!/usr/bin/env python
import os

from flask import Flask
from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient



app = Flask(__name__)


@app.route('/')
def todo():
    es_client = Elasticsearch(
    ['http://elasticsearch:9200'],  # Use your Elasticsearch host
    verify_certs=False,
    ssl_show_warn=False  # Optional: suppresses warnings about insecure SSL
)
    mongo_client = MongoClient("mongo:27017")

    es_client.index(index="my-index-000001", id="45", body={"any": "data", "timestamp": datetime.now()})
    data = es_client.get(index="my-index-000001", id="45")

    db = mongo_client['example_database']
    collection = db['example_collection']

    # Insert a document
    document = {"name": "John Doe", "age": 30}
    insert_result = collection.insert_one(document)
    print(f"Inserted document ID: {insert_result.inserted_id}")

    # Retrieve the document
    retrieved_doc = collection.find_one({"name": "John Doe"})
    print(f"Retrieved document: {retrieved_doc}")

    mongo_client.close()

    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9091), debug=True)
