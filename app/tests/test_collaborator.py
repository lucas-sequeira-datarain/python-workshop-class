from src.classes.collaborator import Collaborator


def test_collaborator_constructor():
    """Tests the Collaborator class constructor."""
    c1 = Collaborator("John", 36, "Sales")
    assert c1.name == "John"
    assert c1.age == 36
    assert c1.area == "Sales"


def test_collaborator_introduce():
    """Tests the Collaborator class introduce method."""
    c1 = Collaborator("John", 36, "Sales")
    assert c1.introduce() == "My name is John and I am 36 years old. I work in Sales."
