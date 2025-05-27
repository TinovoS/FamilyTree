from enum import Enum, auto
from datetime import date
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from person import Person

class RelationshipType(Enum):
    BIOLOGICAL_PARENT = (auto(), "BIOLOGICAL_CHILD", False)
    ADOPTIVE_PARENT = (auto(), "ADOPTIVE_CHILD", False)
    STEP_PARENT = (auto(), "STEP_CHILD", False)
    SPOUSE = (auto(), "SPOUSE", True)
    SIBLING = (auto(), "SIBLING", True)
    HALF_SIBLING = (auto(), "HALF_SIBLING", True)
    AUNT_UNCLE = (auto(), "NIECE_NEPHEW", False)
    COUSIN = (auto(), "COUSIN", True)
    GODPARENT = (auto(), "GODCHILD", False)

    def __new__(cls, value, reciprocal_name, is_symmetric: bool):
        obj = object.__new__(cls)
        obj._value = value
        obj.reciprocal_name = reciprocal_name
        obj.is_symmetric = is_symmetric
        return obj

    @classmethod
    def get_reciprocal(cls, relationship_type: 'RelationshipType') -> 'RelationshipType':
        if relationship_type.is_symmetric:
            return relationship_type
        return cls[relationship_type.reciprocal_name]

    @classmethod
    def build_reverse_index(cls) -> Dict['RelationshipType', 'RelationshipType']:
        return {
            rel: cls.get_reciprocal(rel)
            for rel in cls
        }


class Relationship:
    def __init__(
        self,
        from_person: 'Person',
        to_person: 'Person',
        relationship_type: RelationshipType,
        **kwargs
    ):
        self.from_person = from_person
        self.to_person = to_person
        self.relationship_type = relationship_type
        self.metadata = kwargs

        if 'no_reciprocal' in kwargs:
            self._create_reciprocal()

    def _create_reciprocal(self):
        reciprocal_type = RelationshipType.get_reciprocal(self.relationship_type)
        Relationship(
            from_person=self.to_person,
            to_person=self.from_person,
            relationship_type=reciprocal_type,
            no_reciprocal=True,
            **self.metadata
        )

