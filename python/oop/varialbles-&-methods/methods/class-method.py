class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @classmethod
    def get_first_name(cls, full_name):
        first_name = full_name.split()[0]
        return cls(first_name)


person = Person.get_first_name("Imam Hossain")
print(person.first_name)