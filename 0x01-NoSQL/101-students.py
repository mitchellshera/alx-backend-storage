#!/usr/bin/env python3
'''module for students by avg score'''


def top_students(mongo_collection):
    """ students by avg score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
