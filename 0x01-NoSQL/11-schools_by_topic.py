#!/usr/bin/env python3
'''module for list of schools in topic'''


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic."""
    query = {'topics': {'$in': [topic]}}
    result = mongo_collection.find(query)
    return list(result)
