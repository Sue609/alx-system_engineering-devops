#!/usr/bin/python3
"""
This module introduces a script using te REST API.
"""

import requests
import sys


def get_employee_data(employee_id):
    """
    Script that returns information of a given employee ID about his/her
    todo list progress.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    """ Fteching the users data."""
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    """Fetching useres TODO list"""
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    """ Calculating completes and total tasks"""
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    return employee_name, completed_tasks, total_tasks, todos


def main():
    """
    The main function.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])

    try:
        employee_name, completed_tasks, total_tasks, todos = get_employee_data(
                employee_id)
        print(f"Employee {employee_name} is done with tasks("
              f"{completed_tasks}/{total_tasks}):")

        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
