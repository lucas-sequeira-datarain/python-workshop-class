from src.classes.squad import Squad
from src.classes.collaborator import Collaborator


def test_squad_constructor():
    """Tests the Squad class constructor."""
    # Create a squad with no collaborators:
    s1 = Squad(name="Squad 1")
    assert s1.collaborators == []
    assert s1.name == "Squad 1"

    # Create a squad with collaborators:
    collaborators = [
        Collaborator("John", 36, "Sales"),
        Collaborator("Mary", 29, "Marketing")
    ]
    s2 = Squad(name="Squad 2", collaborators=collaborators)
    assert s2.collaborators == collaborators
    assert s2.name == "Squad 2"


def test_squad_add_collaborator():
    """Tests the Squad class add_collaborator method."""
    s1 = Squad(name="Squad 1")
    c1 = Collaborator("John", 36, "Sales")
    s1.add_collaborator(c1)
    assert s1.collaborators == [c1]

    c2 = Collaborator("Mary", 29, "Marketing")
    s1.add_collaborator(c2)
    assert s1.collaborators == [c1, c2]


def test_squad_remove_collaborator():
    """Tests the Squad class remove_collaborator method."""
    s1 = Squad(name="Squad 1")
    c1 = Collaborator("John", 36, "Sales")
    c2 = Collaborator("Mary", 29, "Marketing")
    s1.add_collaborator(c1)
    s1.add_collaborator(c2)
    s1.remove_collaborator(c1)
    assert s1.collaborators == [c2]


def test_squad_get_collaborators():
    """Tests the Squad class get_collaborators method."""
    s1 = Squad(name="Squad 1")
    c1 = Collaborator("John", 36, "Sales")
    c2 = Collaborator("Mary", 29, "Marketing")
    s1.add_collaborator(c1)
    s1.add_collaborator(c2)
    assert s1.get_collaborators() == [c1, c2]


def test_squad_get_areas():
    """Tests the Squad class get_areas method."""
    s1 = Squad(name="Squad 1")
    c1 = Collaborator("John", 36, "Sales")
    c2 = Collaborator("Mary", 29, "Marketing")
    s1.add_collaborator(c1)
    s1.add_collaborator(c2)
    assert s1.get_areas() == ["Marketing", "Sales"]

    c3 = Collaborator("Peter", 31, "Sales")
    s1.add_collaborator(c3)
    assert s1.get_areas() == ["Marketing", "Sales"]


def test_squad_get_num_collaborators():
    """Tests the Squad class get_num_collaborators method."""
    s1 = Squad(name="Squad 1")
    c1 = Collaborator("John", 36, "Sales")
    c2 = Collaborator("Mary", 29, "Marketing")
    s1.add_collaborator(c1)
    s1.add_collaborator(c2)
    assert s1.get_num_collaborators() == 2

    c3 = Collaborator("Peter", 31, "Sales")
    s1.add_collaborator(c3)
    assert s1.get_num_collaborators() == 3


def test_squad_introduce():
    """Tests the Squad class introduce method."""
    s1 = Squad(name="Squad 1")
    c1 = Collaborator("John", 36, "Sales")
    c2 = Collaborator("Mary", 29, "Marketing")
    s1.add_collaborator(c1)
    s1.add_collaborator(c2)
    assert s1.introduce() == "This is the Squad: Squad 1, there are 2 working on it.\n\tMy name is John and I am 36 years old. I work in Sales.\n\tMy name is Mary and I am 29 years old. I work in Marketing."
