#!/usr/bin/python3
""" Export all employees data in the JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    ids_req = requests.get('https://jsonplaceholder.typicode.com/users')
    ids_json = ids_req.json()
    ids = [id.get('id') for id in ids_json]

    to_dict = {}
    for user_id in ids:
        response_users = requests.get(
                         'https://jsonplaceholder.typicode.com/users')
        employees = response_users.json()
        employees_list = [user for user in employees if user['id'] == user_id]
        user_name = employees_list[0].get('username')

        response_todos = requests.get(
                         'https://jsonplaceholder.typicode.com/todos')
        todos = response_todos.json()
        user_x = [user for user in todos if user['userId'] == user_id]

        to_append = []
        for user in user_x:
            to_append.append({
                "task": user.get("title"),
                "completed": user.get("completed"),
                "username": user_name
            })
        to_dict.update({user_id: to_append})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(to_dict, file)
