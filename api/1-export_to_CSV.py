#!/usr/bin/python3
"""
Exercise 1:
Interacts with the APIs
at https://jsonplaceholder.typicode.com/
and gets info about users'
to-do lists and which tasks have they completed.

This file then writes that information into
a file called f"{USER_ID}.csv".

Head over to https://jsonplaceholder.typicode.com/todos/
and https://jsonplaceholder.typicode.com/users
---
to understand how the JSON data is recieved by this program!!!
---
"""
import csv
import requests

if __name__ == "__main__":
    from sys import argv

    USER_ID = int(argv[1])

    ROOT_URL = "https://jsonplaceholder.typicode.com/"

    TODOS = requests.get(f'{ROOT_URL}todos/').json()
    USERNAMES = requests.get(f'{ROOT_URL}users/').json()

    USERNAME = USERNAMES[USER_ID - 1]['username']

    USER_TASKS = tuple(
        task
        for task in TODOS
        if task['userId'] == USER_ID
    )

    with open(f"{USER_ID}.csv", "w") as output_file:
        csv_writer = csv.writer(output_file, quoting=1)

        for task in USER_TASKS:
            csv_writer.writerow(
                (
                    USER_ID,
                    USERNAME,
                    task['completed'],
                    task['title']
                )
            )
