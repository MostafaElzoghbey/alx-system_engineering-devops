#!/usr/bin/python3

"""
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    tasks = get(
        "https://jsonplaceholder.typicode.com/user/{}/todos".format(argv[1])
    ).json()
    user = get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    name = user.get("name")
    numer_of_tasks = len(tasks)
    numer_of_comleted_tasks = len([task for task in tasks if (task.get("completed"))])
    print(
        "Employee {} is done with tasks({}/{}):".format(
            name, numer_of_comleted_tasks, numer_of_tasks
        )
    )
    for task in tasks:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
