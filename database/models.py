from datetime import date
import uuid
from sqlalchemy import String, Date, Boolean, Enum, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase
from enum import Enum as PyEnum

class Base(DeclarativeBase):
    pass

class Gender(str, PyEnum):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    def __str__(self):
        return self.value

class RelationshipType(str, PyEnum):
    BIOLOGICAL_PARENT = "BIOLOGICAL_PARENT"
    ADOPTIVE_PARENT = "ADOPTIVE_PARENT"
    STEP_PARENT = "STEP_PARENT"
    SPOUSE = "SPOUSE"
    SIBLING = "SIBLING"
    HALF_SIBLING = "HALF_SIBLING"
    AUNT_UNCLE = "AUNT_UNCLE"
    COUSIN = "COUSIN"
    GODPARENT = "GODPARENT"
    BIOLOGICAL_CHILD = "BIOLOGICAL_CHILD"
    ADOPTIVE_CHILD = "ADOPTIVE_CHILD"
    STEP_CHILD = "STEP_CHILD"
    NIECE_NEPHEW = "NIECE_NEPHEW"
    GODCHILD = "GODCHILD"

    def __str__(self):
        return self.value

class PersonDB(Base):
    __tablename__ = 'persons'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[Gender] = mapped_column(
        Enum(Gender, values_callable=lambda x: [e.value for e in Gender],
             native_enum=False)
    )
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    death_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    birth_place: Mapped[str | None] = mapped_column(String(100), nullable=True)
    alive: Mapped[bool] = mapped_column(Boolean, default=True)
    last_update: Mapped[date] = mapped_column(Date, default=date.today())


class RelationshipDB(Base):
    __tablename__ = 'relationships'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    from_person_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('persons.id'))
    to_person_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('persons.id'))
    relationship_type: Mapped[RelationshipType] = mapped_column(
        Enum(RelationshipType, values_callable=lambda x: [e.value for e in RelationshipType],
             native_enum=False, length=20)
    )

    from_person: Mapped[PersonDB] = relationship(foreign_keys=[from_person_id])
    to_person: Mapped[PersonDB] = relationship(foreign_keys=[to_person_id])