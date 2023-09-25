#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


def get_user_data(user_id):
    """
    functionality to retrieve user data and user's TODO list
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(user_id))

    if user_response.status_code != 200:
        return None

    user = user_response.json()
    return user


def get_user_todos(user_id):
    """
    functionality to retrieve user data and user's TODO list
    """
    url = "https://jsonplaceholder.typicode.com/"
    todos_response = requests.get(url + "todos", params={"userId": user_id})

    if todos_response.status_code != 200:
        return None

    todos = todos_response.json()
    return todos


def export_to_csv(user_id, username, todos):
    """
    takes user ID, username, and TODO list as arguments.
    """
    if todos is None:
        return

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([
                user_id,
                username,
                str(todo.get("completed")),
                todo.get("title")
            ])


def main():
    """
     function handles command-line arguments
     calls the data retrieval functions,
     and then exports the data to a CSV file.
     """
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user = get_user_data(user_id)
    if user is None:
        print("User not found")
        sys.exit(1)

    username = user.get("username")
    todos = get_user_todos(user_id)
    export_to_csv(user_id, username, todos)


if __name__ == "__main__":
    main()
