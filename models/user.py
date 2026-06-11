from models.person import Person


class User(Person):

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name)

        self.id = User.id_counter
        User.id_counter += 1

        self.email = email
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value and "@" in value:
            self._email = value
        else:
            raise ValueError("Invalid email")

    def add_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"{self.name} ({self.email})"