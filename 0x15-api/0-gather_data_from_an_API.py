#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys


def get_todo_list(employee_id):
    """
    Python script that, using this REST API, for a given employee ID
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        if user_response.status_code == 200 and \
                todo_response.status_code == 200:
            employee_name = user_data['name']
            total_tasks = len(todo_data)
            completed_tasks = sum(1 for task in todo_data if task['completed'])

            print(f'Employee {employee_name} is done with tasks'
                  f'({completed_tasks}/{total_tasks}):')
            for task in todo_data:
                if task['completed']:
                    print(f'\t{task["title"]}')
        else:
            print(f"Error: Unable to retrieve data for employee {employee_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list(employee_id)
