#!/usr/bin/python3
"""
Exercise 2:
Interacts with the APIs
at https://jsonplaceholder.typicode.com/
and gets info about users and their
to-do lists.

This file then writes that information
in this format:
----------------------------------------------
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        ...
    ],
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        ...
    ]
}
----------------------------------------------
to a file named 'todo_all_employees.json'

Head over to https://jsonplaceholder.typicode.com/todos/
and https://jsonplaceholder.typicode.com/users
---
to understand how the JSON data is recieved by this program!!!
---
"""
import json
import requests

ROOT_URL = "https://jsonplaceholder.typicode.com/"

TODOS = requests.get(f'{ROOT_URL}todos/').json()
USERS = requests.get(f'{ROOT_URL}users/').json()

if __name__ == "__main__":
    with open("todo_all_employees.json", "w") as output_file:
        result = {
            user['id']: [
                {
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']
                }
                for task in TODOS
                if task['userId'] == user['id']
            ]
            for user in USERS
        }

        json.dump(result, output_file)
