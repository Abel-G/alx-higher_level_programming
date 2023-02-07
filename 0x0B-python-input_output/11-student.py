#!/usr/bin/python3
""" student - 3"""


class Student(object):
        """Class student"""

            def __init__(self, first_name, last_name, age):
                        """__init__ initialized constructor """
                                self.first_name = first_name
                                        self.last_name = last_name
                                                self.age = age

                                                    def to_json(self, attrs=None):
                                                                """retrieves a dictionary represt """
                                                                        if attrs is None:
                                                                                        return self.__dict__
                                                                                            dictionary = {}
                                                                                                    for key, value in self.__dict__.items():
                                                                                                                    if key in attrs:
                                                                                                                                        dictionary[key] = value
                                                                                                                                                return dictionary

                                                                                                                                                def reload_from_json(self, json):
                                                                                                                                                            """Replace all attributes of the Student """
                                                                                                                                                                    for key, value in json.items():
                                                                                                                                                                                    setattr(self, key, value)
