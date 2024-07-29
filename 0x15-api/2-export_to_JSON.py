#!/usr/bin/python3
"""Exports data to JSON format."""
import json
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('username')

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        }
        tasks.append(task_info)

    data = {str(employee_id): tasks}

    json_file_name = f'{employee_id}.json'

    with open(json_file_name, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Data exported to {json_file_name}')


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
