#!/usr/bin/python3
""" For a given employee ID, returns information
    about his/her TODO list progress """
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = response_users.json()
    employees_list = [user for user in employees if user['id'] == user_id]
    user_name = employees_list[0]['name']

    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response_todos.json()
    user_x = [user for user in todos if user['userId'] == user_id]
    completed = [user for user in user_x if user['completed'] is True]
    print(f"Employee {user_name} is done with tasks\
({len(completed)}/{len(user_x)}):")
    for true in completed:
        print(f"\t {true['title']}")
