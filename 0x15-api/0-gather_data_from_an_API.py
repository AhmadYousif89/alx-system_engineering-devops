#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


def fetch_data(employeeId):
    """Fetch data from jsonplaceholder API"""
    employee = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employeeId}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employeeId}"
    ).json()
    return (employee, todos)


def display_tasks(employeeId):
    """Display employee's tasks information"""
    employee, todos = fetch_data(employeeId)
    completed_titles = []
    for todo in todos:
        if todo.get("completed") is True:
            completed_titles.append(todo.get("title"))
    print(
        f"Employee {employee.get('name')} is done with "
        f"tasks({len(completed_titles)}/{len(todos)}):"
    )
    [print(f"\t {todo}") for todo in completed_titles]


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employeeId = int(sys.argv[1])
        display_tasks(employeeId)
    else:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        exit(1)
