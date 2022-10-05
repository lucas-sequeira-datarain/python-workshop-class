# Create a class named Person, with a properties named name and age, and a method named introduce:
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"My name is {self.name} and I am {self.age} years old."


def main():
    p1 = Person("John", 36)
    print(p1.introduce())


if __name__ == "__main__":
    main()
