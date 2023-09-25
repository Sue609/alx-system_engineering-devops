#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def to_dict(url):
    """
    Function that exports data in the JSON formart.
    Transforms the dta to a dict.
    """
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    to_dict(url)
