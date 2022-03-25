"""
Single Responsibility Principle
A class should have only one job.
If a class has more than one responsibility, it becomes coupled.
A change to one responsibility results to modification of the other responsibility.
"""

import json


class Author:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def make_json(self):
        data_list = []
        author_name = self.get_name()
        data_list.append({'name': author_name})
        return json.dumps(data_list)


author = Author('Uncle Bob')
author.set_name('Uncle Bob')
print(author.make_json())

""" The above Author class violates the Single Responsibility Principle"""

"""Let's organized the code according to  Single Responsibility Principle"""


class Author:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class JsonMaker:
    @staticmethod
    def make(data_list):
        return json.dumps(data_list)


json_maker = JsonMaker()
print(json_maker.make([{'name': 'Roni'}]))
