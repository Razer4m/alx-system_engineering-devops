#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import requests
import sys
import csv


def get_employee_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('username')

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    csv_file_name = f'{employee_id}.csv'

    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([employee_id,
                                 employee_name,
                                 task.get('completed'), task.get('title')])

    print(f'Data exported to {csv_file_name}')


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
