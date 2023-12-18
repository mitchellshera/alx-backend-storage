#!/usr/bin/env python3
'''module for list all in mongo collection '''


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection."""
    documents = mongo_collection.find()
    return list(documents)
