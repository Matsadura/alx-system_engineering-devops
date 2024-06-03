#!/usr/bin/python3
""" Export data in the CSV format """
import csv
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

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for user in user_x:
            writer.writerow([user_id,
                            user_name,
                            user['completed'],
                            user['title']])
