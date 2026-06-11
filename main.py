import argparse

from rich import print

from models.user import User
from models.project import Project
from models.task import Task

from services.storage_service import StorageService
from services.ai_client import AIClient


storage = StorageService()
users = storage.load_data()

ai_client = AIClient()


# --------------------------
# Helper Functions
# --------------------------

def find_user(name):

    for user in users:
        if user.name.lower() == name.lower():
            return user

    return None


def find_project(title):

    for user in users:

        for project in user.projects:

            if project.title.lower() == title.lower():
                return project

    return None


# --------------------------
# Command Functions
# --------------------------

def add_user(args):

    try:

        user = User(
            args.name,
            args.email
        )

        users.append(user)

        storage.save_data(users)

        print("[green]User added successfully.[/green]")

    except Exception as e:

        print(f"[red]{e}[/red]")


def list_users():

    if len(users) == 0:

        print("[yellow]No users found.[/yellow]")
        return

    print("\n[bold]Users[/bold]\n")

    for user in users:
        print(user)


def add_project(args):

    user = find_user(args.user)

    if user is None:

        print("[red]User not found.[/red]")
        return

    project = Project(
        args.title,
        args.description,
        args.due_date
    )

    user.add_project(project)

    storage.save_data(users)

    print("[green]Project added successfully.[/green]")


def list_projects(args):

    user = find_user(args.user)

    if user is None:

        print("[red]User not found.[/red]")
        return

    if len(user.projects) == 0:

        print("[yellow]No projects found.[/yellow]")
        return

    print("\n[bold]Projects[/bold]\n")

    for project in user.projects:
        print(project.title)


def add_task(args):

    project = find_project(args.project)

    if project is None:

        print("[red]Project not found.[/red]")
        return

    task = Task(
        args.title,
        args.assigned_to
    )

    project.add_task(task)

    storage.save_data(users)

    print("[green]Task added successfully.[/green]")


def list_tasks(args):

    project = find_project(args.project)

    if project is None:

        print("[red]Project not found.[/red]")
        return

    if len(project.tasks) == 0:

        print("[yellow]No tasks found.[/yellow]")
        return

    print("\n[bold]Tasks[/bold]\n")

    for task in project.tasks:
        print(task)


def complete_task(args):

    project = find_project(args.project)

    if project is None:

        print("[red]Project not found.[/red]")
        return

    success = project.complete_task(args.task)

    if success:

        storage.save_data(users)

        print("[green]Task completed successfully.[/green]")

    else:

        print("[red]Task not found.[/red]")


def summarize_project(args):

    project = find_project(args.project)

    if project is None:

        print("[red]Project not found.[/red]")
        return

    print("\n[bold]AI Project Summary[/bold]\n")

    summary = ai_client.summarize_project(project)

    print(summary)


# --------------------------
# CLI Setup
# --------------------------

parser = argparse.ArgumentParser(
    description="Project Management CLI Tool"
)

subparsers = parser.add_subparsers(dest="command")


# Add User

add_user_parser = subparsers.add_parser(
    "add-user",
    help="Add a new user"
)

add_user_parser.add_argument(
    "--name",
    required=True
)

add_user_parser.add_argument(
    "--email",
    required=True
)


# List Users

subparsers.add_parser(
    "list-users",
    help="List all users"
)


# Add Project

add_project_parser = subparsers.add_parser(
    "add-project",
    help="Add a project"
)

add_project_parser.add_argument(
    "--user",
    required=True
)

add_project_parser.add_argument(
    "--title",
    required=True
)

add_project_parser.add_argument(
    "--description",
    default=""
)

add_project_parser.add_argument(
    "--due-date",
    default=""
)


# List Projects

list_projects_parser = subparsers.add_parser(
    "list-projects",
    help="List projects for a user"
)

list_projects_parser.add_argument(
    "--user",
    required=True
)


# Add Task

add_task_parser = subparsers.add_parser(
    "add-task",
    help="Add a task"
)

add_task_parser.add_argument(
    "--project",
    required=True
)

add_task_parser.add_argument(
    "--title",
    required=True
)

add_task_parser.add_argument(
    "--assigned-to",
    default=""
)


# List Tasks

list_tasks_parser = subparsers.add_parser(
    "list-tasks",
    help="List tasks in a project"
)

list_tasks_parser.add_argument(
    "--project",
    required=True
)


# Complete Task

complete_task_parser = subparsers.add_parser(
    "complete-task",
    help="Mark a task as completed"
)

complete_task_parser.add_argument(
    "--project",
    required=True
)

complete_task_parser.add_argument(
    "--task",
    required=True
)


# Summarize Project

summary_parser = subparsers.add_parser(
    "summarize-project",
    help="Generate AI summary"
)

summary_parser.add_argument(
    "--project",
    required=True
)


args = parser.parse_args()


# --------------------------
# Command Routing
# --------------------------

if args.command == "add-user":

    add_user(args)

elif args.command == "list-users":

    list_users()

elif args.command == "add-project":

    add_project(args)

elif args.command == "list-projects":

    list_projects(args)

elif args.command == "add-task":

    add_task(args)

elif args.command == "list-tasks":

    list_tasks(args)

elif args.command == "complete-task":

    complete_task(args)

elif args.command == "summarize-project":

    summarize_project(args)

else:

    parser.print_help()