from enum import Enum, auto
from datetime import date
from typing import List

class RelationshipType(Enum):
    Parent = auto()
    Child = auto()

class Relationship:
    def __init__(
            self,
            from_person: 'Person',
            to_person: 'Person',
            relationship_type: RelationshipType,
            start_date: date = None,
            end_date: date = None,
            #is_legal: bool = False,
            notes: str = ''):
        self.from_person = from_person
        self.to_person = to_person
        self.relationship_type = relationship_type
        self.start_date = start_date
        self.end_date = end_date
        #self.is_legal = is_legal
        self.notes = notes
        #self.evidence = []
        #self.verified = False

    def is_active(self) -> bool:
        return self.end_date is None or  self.end_date > date.today()
