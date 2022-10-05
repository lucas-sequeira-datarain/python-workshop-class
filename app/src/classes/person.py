class Person:
    def __init__(self, name: str, age: int):
        """
        Creates a new person.

        Params:
        -------
            name: str - The name of the person.
            age: int - The age of the person.
        """
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Prints a message with the name and age of the person."""
        return f"My name is {self.name} and I am {self.age} years old."
