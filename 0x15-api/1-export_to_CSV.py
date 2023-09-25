#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def export_to_json(user_id):
    """
    Handles the export to JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    data = {str(user_id): []}

    for todo in todos:
        task_data = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        data[str(user_id)].append(task_data)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_json(employee_id)

