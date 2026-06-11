class Project:

    id_counter = 1

    def __init__(self, title, description="", due_date=""):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date

        self.tasks = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value and value.strip():
            self._title = value
        else:
            raise ValueError("Project title cannot be empty")

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task

        return None

    def __str__(self):
        return self.title
    
    def complete_task(self, task_title):

        task = self.get_task(task_title)

        if task:
            task.mark_complete()
            return True

        return False