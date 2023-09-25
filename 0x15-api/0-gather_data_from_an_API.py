#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys


def get_todo_list(employee_id):
    """
    Python script that, using this REST API, for a given employee ID
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))

    if user_response.status_code != 200:
        return None

    user = user_response.json()
    todos_response = requests.get(url + "todos",
                                  params={"userId": employee_id})
    todos = todos_response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    return user.get("name"), len(completed), len(todos), completed


def main():
    """
    Main function.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    result = get_todo_list(employee_id)

    if result is None:
        print("User not found")
        sys.exit(1)

    employee_name, completed_tasks, total_tasks, completed_list = result

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    for task in completed_list:
        print("\t{}".format(task))


if __name__ == "__main__":
    main()
