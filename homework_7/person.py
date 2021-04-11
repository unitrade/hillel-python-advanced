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

    def copy_with(self, **kwargs):
        my_object = copy(self)
        my_object.__id = uuid.uuid1()
        for key, value in kwargs.items():
            try:
                if key == 'id':
                    print('ID is autogenerate field')
                elif key == 'name':
                    my_object.__name = value
                elif key == 'last_name':
                    my_object.__last_name = value
                elif key == 'gender':
                    my_object.__gender = value
                else:
                    raise NameError("name '{}' is not defined".format(key))
            except NameError as err:
                print(err)
        return my_object

    def get_full_info(self):
        return "+++++++++++++++++++++\nUUID: %s\nName: %s\nSurname: %s\nGender: %s " \
               % (self.__id, self.__name, self.__last_name, self.__gender)

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        return self.__id == other.__id


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

    person1.__setattr__("name", "Alex")
    assert person1.get_name() == 'Silvester', 'Object has been changed'

    person4 = person1.copy_with(
        id="123",
        city="New York",
        name="Rihanna",
        last_name="Fenty",
        gender='female',
        birthday="1988"
    )

    print(person1.get_full_info())
    print(person4.get_full_info())

    # ID is autogenerate field
    # name 'city' is not defined
    # name 'birthday' is not defined
    # +++++++++++++++++++++
    # UUID: 809ca276-9ad3-11eb-b421-acde48001122
    # Name: Silvester
    # Surname: Stallone
    # Gender: male
    # +++++++++++++++++++++
    # UUID: 809ca4f6-9ad3-11eb-b421-acde48001122
    # Name: Rihanna
    # Surname: Fenty
    # Gender: female
