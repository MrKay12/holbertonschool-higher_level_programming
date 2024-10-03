#!/usr/bin/python3
import pickle

class CustomObject:
    """A custom Python class representing a person"""
    def __init__(self, name, age, is_student):
        """Initializes the CustomObject with the given attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the CustomObject
        instance in a formatted output"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance of CustomObject to a file"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserializes a file and returns an instance of CustomObject"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
