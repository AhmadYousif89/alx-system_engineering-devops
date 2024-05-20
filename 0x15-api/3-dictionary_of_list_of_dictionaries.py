#!/usr/bin/python3
"""Gather data from an API"""
import requests
import json


def fetch_data():
    """
    Fetches data from the JSONPlaceholder API and stores it in a JSON file.

    Returns:
        list: A list of dictionaries containing information about employees and their tasks.
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
    tasks_by_user = {}
    for task in all_tasks:
        user_id = task["userId"]
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []
        tasks_by_user[user_id].append(
            {
                "username": usernames[user_id],
                "task": task["title"],
                "completed": task["completed"],
            }
        )

    # Convert the dictionary to a list of dictionaries
    employees_info = [
        {user_id: tasks} for user_id, tasks in tasks_by_user.items()
    ]

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(employees_info, file)


if __name__ == "__main__":
    fetch_data()
