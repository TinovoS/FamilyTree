from datetime import date
import uuid
from enum import Enum
from tkinter import Place


class Gender(Enum):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

class Person:
    def __init__(self, first_name, last_name, gender):
        self.__id = uuid.uuid4()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__alive = True
        self.__last_update = date.today()

        self.__birth_date = None
        self.__death_date = None
        self.__birth_place = None
        self.__age = None
        self.__parents = []
        self.__children = []
        self.__notes = "" #like later people can post stuff about them on socials like comments and etc share their expirience
        self.__photos = [] #same goes for photos people can share about them

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def lastName(self) -> str:
        return self.__last_name

    @property
    def birth_date(self) -> date:
        return self.__birth_date

    @property
    def death_date(self) -> date:
        return self.__death_date

    @property
    def age(self) -> int:
        return self.__age

    @property
    def birth_place(self) -> str:
        return self.__birth_place

    @first_name.setter
    def first_name(self, name):
        self.__first_name = name
        self.__update_last_modified()

    @birth_date.setter
    def birth_date(self, value: date):
        if isinstance(value, date) or value is None:
            self.__birth_date = value
            self.calculate_age()
            self.__update_last_modified()

    @death_date.setter
    def death_date(self, value: date):
        if isinstance(value, date) or value is None:
            self.__death_date = value
            self.check_alive()
            self.calculate_age()
            self.__update_last_modified()

    @birth_place.setter
    def birth_place(self, value: str):
        self.__birth_place = value

    def calculate_age(self) -> int:
        if self.__alive:
            return (date.today() - self.__birth_date).year
        else:
            return (self.__death_date - self.__birth_date).year

    def add_child(self, child: 'Person'):
        if child not in self.__children:
            self.__children.append(child)
            child.add_parent(self)
            self.__update_last_modified()

    def add_parent(self, parent: 'Person'):
        if parent not in self.__parents:
            if len(self.__parents) < 2:
                self.__parents.append(parent)
                self.__update_last_modified()

    def check_alive(self):
        if self.__death_date is not None:
            self.__alive = False
            self.__update_last_modified()

    def __update_last_modified(self):
        self.__last_update = date.today()