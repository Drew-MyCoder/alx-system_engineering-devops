#!/usr/bin/python3
"""
This is a Python script that, uses this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":

    import requests
    import sys
    import json

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        ui_url = 'https://jsonplaceholder.typicode.com/users/'
        tds_url = 'https://jsonplaceholder.typicode.com/todos?userId='

        USER_ID = requests.get(ui_url + sys.argv[1]).json()['id']
        USERNAME = requests.get(ui_url + sys.argv[1]).json()['username']
        TASK_COMPLETED_STATUSES = [task['completed'] for task in
                                   requests.get(tds_url + sys.argv[1]).json()]
        TASKS_TITLES = [task['title'] for task in
                        requests.get(tds_url + sys.argv[1]).json()]
        TOTAL_NUMBER_OF_TASKS = len(requests.get(tds_url + sys.argv[1]).json())

        TASKS_DICT = {"{}".format(USER_ID):
                      [{"task": "{}".format(TASKS_TITLES[N]),
                        "completed": TASK_COMPLETED_STATUSES[N],
                        "username": "{}".format(USERNAME)}
                       for N in range(TOTAL_NUMBER_OF_TASKS)]}

        with open('{}.json'.format(USER_ID), 'w') as fp:
            json.dump(TASKS_DICT, fp)
