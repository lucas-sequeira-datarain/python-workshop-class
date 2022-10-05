from src.classes.collaborator import Collaborator
from typing import List


class Squad():
    def __init__(self, name: str, collaborators: List[Collaborator] = None):
        """
        Creates a new squad.

        Params:
        -------
            name: str - The name of the squad.
            collaborators: List[Collaborator] - List of collaborators.
        """
        self.name = name
        if collaborators is None:
            self.collaborators = []
        else:
            self.__set_collaborators(collaborators)

    def __set_collaborators(self, collaborators: List[Collaborator]):
        """Update the collaborators of the squad."""
        self.collaborators = collaborators

    def add_collaborator(self, collaborator: Collaborator):
        """Add a collaborator to the squad."""
        self.collaborators.append(collaborator)

    def remove_collaborator(self, collaborator: Collaborator):
        """Remove a collaborator from the squad."""
        self.collaborators.remove(collaborator)

    def get_collaborators(self) -> List[Collaborator]:
        """Return the collaborators of the squad."""
        return self.collaborators

    def get_areas(self) -> List[str]:
        """Return the areas of the squad."""
        areas = set()
        for collaborator in self.collaborators:
            areas.add(collaborator.area)
        return sorted(list(areas))

    def get_num_collaborators(self) -> int:
        """Return the number of collaborators of the squad."""
        return len(self.collaborators)

    def introduce(self) -> str:
        """Prints a message with the name of the squad and the collaborators intros."""
        intro = f"This is the Squad: {self.name}, there are {self.get_num_collaborators()} working on it."
        for collaborator in self.get_collaborators():
            intro += f"\n\t{collaborator.introduce()}"

        return intro
