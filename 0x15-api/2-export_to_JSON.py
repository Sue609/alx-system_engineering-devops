#!/usr/bin/python3
"""
This module introduces a function.
"""

import json
import sys

# Load the data (assuming you have the data in a dictionary called "data")
data = {
    "1": [
        {"task": "Task 1", "completed": False, "username": "User1"},
        {"task": "Task 2", "completed": True, "username": "User1"},
    ],
    "2": [
        {"task": "Task A", "completed": True, "username": "User2"},
        {"task": "Task B", "completed": False, "username": "User2"},
    ],
    "3": [
        {"task": "Task X", "completed": True, "username": "User3"},
        {"task": "Task Y", "completed": False, "username": "User3"},
    ],
}


def export_to_json(user_id, data):
    """
    Exporting the json file.
    """
    if user_id not in data:
        print(f"No tasks found for user with ID {user_id}")
        return

    user_tasks = data[user_id]
    output_file = f"{user_id}.json"

    with open(output_file, "w") as file:
        json.dump({user_id: user_tasks}, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_JSON.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_json(user_id, data)
