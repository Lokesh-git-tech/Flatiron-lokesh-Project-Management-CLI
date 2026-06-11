class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value and value.strip():
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    def __str__(self):
        return self.name