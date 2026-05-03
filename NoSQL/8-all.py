#!/usr/bin/env python3
"""
Module for task 8: List all documents in Python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents, or an empty list if no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
