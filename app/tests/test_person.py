from src.classes.person import Person


def test_person_construct():
    """Tests the Person class constructor."""
    p1 = Person("John", 36)
    assert p1.name == "John"
    assert p1.age == 36


def test_person_introduce():
    """Tests the Person class introduce method."""
    p1 = Person("John", 36)
    assert p1.introduce() == "My name is John and I am 36 years old."
