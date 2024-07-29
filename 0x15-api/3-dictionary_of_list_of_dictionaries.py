#!/usr/bin/python3
"""Exports the to-do list information for all employees to a JSON file."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users_data = requests.get(f"{base_url}users").json()

    # Prepare to-do data for all users
    all_todos = {
        user.get("id"): [
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": user.get("username")}
            for task in requests.get(f"{base_url}todos",
                                     params={"userId": user.get("id")}).json()
        ]
        for user in users_data
    }

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_todos, json_file)
