#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a CSV file."""

import requests
import sys
import csv

def get_todo_list(employee_id):
    """
     This function takes an employee_id as input and returns user data and their TODO list
     """
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        return None, None

    user = user_response.json()
    
    # Fetch user's TODO list
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    todos = todos_response.json()

    return user, todos


def export_to_csv(user, todos):
    """
    This function takes user data and the TODO list as input
    and exports the data to a CSV file in the specified format
    """
    if user is None or todos is None:
        return

    filename = "{}.csv".format(user["id"])
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([user["id"], user["username"], str(todo["completed"]), todo["title"]])


def main():
    """
     It handles command-line arguments, calls the get_todo_list
     and export_to_csv functions, and orchestrates the script's execution.
     """
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user, todos = get_todo_list(employee_id)
    export_to_csv(user, todos)


if __name__ == "__main__":
    main()
