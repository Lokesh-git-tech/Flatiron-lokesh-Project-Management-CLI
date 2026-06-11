import json
import os

from models.user import User
from models.project import Project
from models.task import Task


class StorageService:

    def __init__(self, filename="data/project_data.json"):
        self.filename = filename

    def save_data(self, users):
        data = []

        for user in users:
            user_data = {
                "name": user.name,
                "email": user.email,
                "projects": []
            }

            for project in user.projects:

                project_data = {
                    "title": project.title,
                    "description": project.description,
                    "due_date": project.due_date,
                    "tasks": []
                }

                for task in project.tasks:

                    task_data = {
                        "title": task.title,
                        "status": task.status,
                        "assigned_to": task.assigned_to
                    }

                    project_data["tasks"].append(task_data)

                user_data["projects"].append(project_data)

            data.append(user_data)

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):

        if not os.path.exists(self.filename):
            return []

        try:

            with open(self.filename, "r") as file:
                data = json.load(file)

        except json.JSONDecodeError:
            return []

        users = []

        for user_data in data:

            user = User(
                user_data["name"],
                user_data["email"]
            )

            for project_data in user_data["projects"]:

                project = Project(
                    project_data["title"],
                    project_data["description"],
                    project_data["due_date"]
                )

                for task_data in project_data["tasks"]:

                    task = Task(
                        task_data["title"],
                        task_data["assigned_to"]
                    )

                    task.status = task_data["status"]

                    project.add_task(task)

                user.add_project(project)

            users.append(user)

        return users