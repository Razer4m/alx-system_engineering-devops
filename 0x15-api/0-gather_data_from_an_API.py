#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

import requests
import sys

def get_employee_todo_list_progress(employee_id):
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch employee details
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Fetch employee's TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()
    
    # Calculate TODO list progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    
    # Display the results
    print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task.get("title")}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
