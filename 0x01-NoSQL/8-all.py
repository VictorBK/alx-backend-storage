#!/usr/bin/env python3
""" Python function to list all documents in a collection """
import pymongo

def list_all(mongo_collection) -> list:
    """ Lists all documents in a collection
        Args:
            mongo_collection: Collection of object
        Return:
            List with documents, otherwise []
    """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
