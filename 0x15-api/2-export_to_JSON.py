#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def export_to_json(user_id):
    """
    Python script that exports data in the json format.
    """
    b_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(b_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(b_url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)


if __name__ == "__main__":
    user_id = sys.argv[1]
    export_to_json(user_id)
