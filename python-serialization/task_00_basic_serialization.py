#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    
    Parameters:
    data (dict): The Python dictionary to be serialized.
    filename (str): The name of the JSON file to save the serialized data.
    
    Returns:
    None
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.
    
    Parameters:
    filename (str): The name of the JSON file to read from.
    
    Returns:
    dict: The deserialized Python dictionary from the JSON file.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
