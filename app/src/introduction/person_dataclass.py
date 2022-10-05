from dataclasses import dataclass


# Create a dataclass named Person, with a properties named name and age:
@dataclass
class Person:
    name: str
    age: int


def main():
    p1 = Person("John", 36)
    print(f"{p1=}")
    print(f"{p1.name=}")
    print(f"{p1.age=}")


if __name__ == "__main__":
    main()
