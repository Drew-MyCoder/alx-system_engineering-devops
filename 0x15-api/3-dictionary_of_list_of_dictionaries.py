#!/usr/bin/python3
"""
This is a Python script that, uses this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":

    import requests
    import sys
    import json

    if len(sys.argv) == 1:
        ui_url = 'https://jsonplaceholder.typicode.com/users/'
        tds_url = 'https://jsonplaceholder.typicode.com/todos?userId='

        ALL_USER_IDS = [user['id'] for user in requests.get(ui_url).json()]

        TASKS_DICT_ALL_USERS = {}
        for USER_ID in ALL_USER_IDS:
            USERNAME = requests.get(ui_url + str(USER_ID)).json()['username']
            TASK_COMPLETED_STATUSES = [task['completed'] for task in
                                       requests.get(tds_url + str(USER_ID))
                                       .json()]
            TASKS_TITLES = [task['title'] for task in
                            requests.get(tds_url + str(USER_ID)).json()]
            TOTAL_NUMBER_OF_TASKS = len(requests.get(tds_url + str(USER_ID))
                                        .json())
            TASKS_DICT = {"{}".format(USER_ID):
                          [{"task": "{}".format(TASKS_TITLES[N]),
                            "completed": TASK_COMPLETED_STATUSES[N],
                            "username": "{}".format(USERNAME)}
                           for N in range(TOTAL_NUMBER_OF_TASKS)]}
            TASKS_DICT_ALL_USERS["{}".format(USER_ID)] = TASKS_DICT[
                "{}".format(USER_ID)]

        with open('todo_all_employees.json', 'w') as fp:
            json.dump(TASKS_DICT_ALL_USERS, fp)
