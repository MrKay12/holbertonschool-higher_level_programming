#!/usr/bin/python3
def search_replace(my_list, search, replace):

    list2 = [replace if element == search else element for element in my_list]
    new_list = list2
    return new_list
