#!/usr/bin/python3
"""
This module introduces a function.
"""


import json
import requests

def export_all_employees_to_json():
    """
    Fetch the data from the API endpoint
    """
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()

    # Create a dictionary to store tasks for each user
    user_tasks = {}

    # Iterate through the todos and organize them by user ID
    for todo in todos:
        user_id = todo['userId']
        task = {
            "username": "",  # You can fetch the username from another API or source
            "task": todo['title'],
            "completed": todo['completed']
        }

        # Add the task to the user's list of tasks
        if user_id in user_tasks:
            user_tasks[user_id].append(task)
        else:
            user_tasks[user_id] = [task]

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)


if __name__ == "__main__":
    export_all_employees_to_json()

