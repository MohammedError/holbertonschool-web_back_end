#!/usr/bin/env python3
"""
Module for task 11: Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic searched.

    Returns:
        List of schools having the specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
