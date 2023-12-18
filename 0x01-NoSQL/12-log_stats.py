#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats(mongo_collection):
    """
    Prints some stats about Nginx logs stored in MongoDB
    """
    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Stats for specific method and path
    method_path_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(method_path_count))

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the collection
    nginx_collection = client.logs.nginx

    # Call the log_stats function
    log_stats(nginx_collection)