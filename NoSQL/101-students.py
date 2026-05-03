#!/usr/bin/env python3
"""
Module for task 101: Top students
"""


def top_students(mongo_collection):
    """
    Returns all students in a collection sorted by average score.
    The averageScore is calculated from the 'score' field in 'topics'.
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
