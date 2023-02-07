#!/usr/bin/python3
""" student """


class Student(object):
        """Class student"""
            def __init__(self, first_name, last_name, age):
                        """__init__ initialized constructor """
                                self.first_name = first_name
                                        self.last_name = last_name
                                                self.age = age

                                                    def to_json(self):
                                                                """retrieves a dictionary represt """
                                                                        return self.__dict__
