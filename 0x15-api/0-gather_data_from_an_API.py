#!/usr/bin/python3
"""
This module introduces a new function.
"""
import requests
import sys


def data_from_api(url):
    """
    Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
    """
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    data_from_api(url)
