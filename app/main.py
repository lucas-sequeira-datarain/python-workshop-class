from src.classes.collaborator import Collaborator
from src.classes.squad import Squad


def main():
    # Initialize the collaborators
    c1 = Collaborator("John", 36, "Sales")
    c2 = Collaborator("Mary", 29, "Marketing")
    c3 = Collaborator("Peter", 30, "Sales")
    c4 = Collaborator("Paul", 31, "Marketing")
    c5 = Collaborator("George", 32, "Sales")

    # Initialize the squads
    s1 = Squad(name="Squad 1", collaborators=[c1, c2])
    s2 = Squad(name="Squad 2", collaborators=[c3, c4, c5])

    # Print the squads
    print(s1.introduce())
    print(s2.introduce())


if __name__ == "__main__":
    main()

# For running tests:
# pytest ./app/ -v --cov=app/ --cov-report=html

# For running lint on code:
# flake8 --ignore E305,E501,E126 --exclude .git,__pycache__,.venv
