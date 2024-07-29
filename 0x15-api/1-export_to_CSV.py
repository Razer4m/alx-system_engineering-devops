#!/usr/bin/python3
"""Exports an employee's to-do list information to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user details
    user_data = requests.get(f"{base_url}users/{employee_id}").json()
    user_name = user_data.get("username")
    
    # Fetch to-do list
    todos_data = requests.get(f"{base_url}todos", params={"userId": employee_id}).json()
    
    # Write to JSON file
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump({
            employee_id: [
                {"task": task.get("title"), "completed": task.get("completed"), "username": user_name}
                for task in todos_data
            ]
        }, json_file)
