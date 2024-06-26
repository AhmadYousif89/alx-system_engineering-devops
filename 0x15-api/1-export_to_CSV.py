#!/usr/bin/python3
"""Gather data from an API"""
import csv
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
    """Display employee's tasks information and export to csv format"""
    employee, todos = fetch_data(employeeId)
    completed_titles = []

    with open(f"{employeeId}.csv", mode='w') as file:
        writer = csv.writer(
            file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL
        )
        for todo in todos:
            writer.writerow(
                [
                    employeeId,
                    employee.get('username'),
                    todo.get('completed'),
                    todo.get('title'),
                ]
            )
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
