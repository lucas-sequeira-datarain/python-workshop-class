# Create a class named Person, with a properties named name and age:
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Create a class named Collaborator, that inherits from Person, with a new property named area:
class Collaborator(Person):
    def __init__(self, name, age, area):
        super().__init__(name, age)
        self.area = area        

def main():
    p1 = Collaborator("John", 36, "Sales")
    print(f"{p1.name=}")
    print(f"{p1.age=}")
    print(f"{p1.area=}")
    print(p1.introduce())

if __name__ == "__main__":
    main()
