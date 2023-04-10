#!/usr/bin/python3
"""
Exercise 2:
Interacts with the APIs
at https://jsonplaceholder.typicode.com/
and gets info about users'
to-do lists and which tasks have they completed.

This file then writes the USER_ID's string
form and all the user's tasks in a dictionary
into a file called f"{USER_ID}.json".
The task dictionary itself is the task's title,
named 'task'; weather or not the user completed
the task, titled 'completed'; and the USERNAME,
titled 'username'.

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
USERNAMES = requests.get(f'{ROOT_URL}users/').json()

if __name__ == "__main__":
    from sys import argv

    USER_ID = int(argv[1])

    USERNAME = USERNAMES[USER_ID - 1]['username']
    USER_TASKS = tuple(
        task
        for task in TODOS
        if task['userId'] == USER_ID
    )

    result = {
        str(USER_ID): [
            {
                'task': task['title'],
                'completed': task['completed'],
                'username': USERNAME
            } for task in USER_TASKS
        ]
    }

    with open(f'{USER_ID}.json', "w") as output_file:
        json.dump(result, output_file)
