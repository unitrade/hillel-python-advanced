import uuid


class Person:
    """
    Person class for Homework 7
    """

    def __init__(self, name, last_name, gender):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__last_name = last_name
        self.__gender = gender

    @staticmethod
    def warn(object_field):
        """

        Method return message if the object is trying to change

        """
        print("The object is not mutable. Can not change to %s" % object_field)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        Person.warn(id)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Person.warn(name)

    @property
    def surname(self):
        return self.__last_name

    @surname.setter
    def surname(self, last_name):
        Person.warn(last_name)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        Person.warn(gender)

    @property
    def full_info(self):
        return "UUID: %s\nName: %s\nSurname: %s\nGender: %s " % (self.__id, self.__name, self.__last_name, self.__gender)

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        return self.__last_name == other.__surname and self.__name == other.__name and self.__gender == other.__gender


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

    # person1._Person__name = 'Igor'
    person1.name = 'Sasha'

    assert person1.name == 'Silvester', 'Object has been changed'
    print(person1.full_info)

    # UUID: d65a1594-97d2-11eb-908b-acde48001122
    # Name: Silvester
    # Surname: Stallone
    # Gender: male
