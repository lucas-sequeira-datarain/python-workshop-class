# Create a class named Person, with a properties named name and age:
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def main():
    p1 = Person("John", 36)
    print(f"{p1=}")
    print(f"{p1.name=}")
    print(f"{p1.age=}")


if __name__ == "__main__":
    main()
