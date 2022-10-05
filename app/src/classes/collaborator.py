from src.classes.person import Person


class Collaborator(Person):
    def __init__(self, name: str, age: int, area: str):
        """
        Creates a new collaborator.

        Params:
        -------
            name: str - The name of the collaborator.
            age: int - The age of the collaborator.
            area: str - The area of the collaborator.
        """
        super().__init__(name, age)
        self.area = area

    def introduce(self) -> str:
        """Prints a message with the name, age and area of the collaborator."""
        return f"My name is {self.name} and I am {self.age} years old. I work in {self.area}."
