#!/usr/bin/env python3
"""Script that provides stats about Nginx logs in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total logs
    print("{} logs".format(collection.count_documents({})))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]

    results = list(collection.aggregate(pipeline))
    counts = {r["_id"]: r["count"] for r in results}

    for method in methods:
        print("\tmethod {}: {}".format(method, counts.get(method, 0)))

    # status check
    status = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print("{} status check".format(status))
