class Task:

    id_counter = 1

    def __init__(self, title, assigned_to=""):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value and value.strip():
            self._title = value
        else:
            raise ValueError("Task title cannot be empty")

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} - {self.status}"