import uuid
from copy import copy


class Person:
    """
    Person class for Homework 7
    """

    def __init__(self, name, last_name, gender):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__last_name = last_name
        self.__gender = gender

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def copy_with(self, name, last_name):
        my_object = copy(self)
        my_object.__id = uuid.uuid1()
        my_object.__name = name
        my_object.__last_name = last_name
        return my_object

    def get_full_info(self):
        return "UUID: %s\nName: %s\nSurname: %s\nGender: %s " \
               % (self.__id, self.__name, self.__last_name, self.__gender)

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        return self.__last_name == other.__last_name and self.__name == other.__name and self.__gender == other.__gender


if __name__ == '__main__':
    person1 = Person(
        'Silvester',
        'Stallone',
        'male'
    )

    person2 = Person(
        'Jackie',
        'Chan',
        'male'
    )

    person3 = Person(
        'Silvester',
        'Stallone',
        'male'
    )

    assert person1 == person3, 'Object not equal'

    person1.__setattr__("name", "Alex")
    assert person1.get_name() == 'Silvester', 'Object has been changed'

    person4 = person1.copy_with(
        "Brad",
        "Pitt"
    )

    print(person1.get_full_info())

    # UUID: 343b4f7a-9936-11eb-a497-acde48001122
    # Name: Silvester
    # Surname: Stallone
    # Gender: male

    print(person4.get_full_info())

    # UUID: 343b520e-9936-11eb-a497-acde48001122
    # Name: Brad
    # Surname: Pitt
    # Gender: male
