# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age
        self.members = []


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.clubs = []

    def assign_president(self, person):
        # your code goes here!
        for person in self.name:
            person = "President"
            # person.append(person)

        # for person.name in self.name:
        #     person.name.append("President")

        # for person in self.name:
        #     if person == my_name:
        #         return person = assign_president()

        # if(create_club()):
        #     self.assign_president(person)
            # person = Person(person.name, person.bio, person.age)
        # self.assign_president(person)

    def recruit_member(self, person):
        # your code goes here!
        # if person in self.clubs:
        #     self.recruit_member(person)
        for person in person.members:
            self.clubs.append(person)

    def print_member_list(self):
        # your code goes here!
        # for self in self.clubs:
        #     print("%s, %s, %s" % (person.name, person.bio, person.age))

        return "%s, %s, %s" % (person.name, person.bio, person.age)

        # for person in self.name:
        #     print(person.name, person.bio, person.age)

