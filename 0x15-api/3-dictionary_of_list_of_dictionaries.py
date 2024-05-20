#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests


def fetch_data():
    """
    Fetches data from the JSONPlaceholder API and stores it in a JSON file.

    Description:
        Creates a list of dictionaries containing information about
        the employees' tasks. Each dictionary contains the following keys:
            - "username": The username of the employee.
            - "task": The title of the task.
            - "completed": A boolean checks if the task is completed or not.
    """
    all_employees = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
    ).json()

    # Create a dictionary mapping userIds to usernames
    usernames = {
        employee["id"]: employee["username"] for employee in all_employees
    }

    # Fetch all tasks
    all_tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos"
    ).json()

    # Group tasks by userId
    user_todos = {}
    for task in all_tasks:
        user_id = task["userId"]
        if user_id not in user_todos:
            user_todos[user_id] = []
        user_todos[user_id].append(
            {
                "username": usernames[user_id],
                "task": task["title"],
                "completed": task["completed"],
            }
        )

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(user_todos, file)


if __name__ == "__main__":
    fetch_data()
