from services.storage_service import StorageService
from models.user import User
from models.project import Project
from models.task import Task

user = User("Alex", "alex@gmail.com")

project = Project(
    "CLI Tool",
    "Python project",
    "2026-08-01"
)

task = Task(
    "Write README",
    "Alex"
)

project.add_task(task)

user.add_project(project)

storage = StorageService()

storage.save_data([user])

users = storage.load_data()

print(users[0])
print(users[0].projects[0])
print(users[0].projects[0].tasks[0])