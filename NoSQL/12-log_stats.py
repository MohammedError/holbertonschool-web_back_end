#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs."""
from pymongo import MongoClient


if __name__ == "__main__":
    collection = MongoClient().logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(
            method, collection.count_documents({"method": method})
        ))
    print("{} status check".format(
        collection.count_documents({"method": "GET", "path": "/status"})
    ))
