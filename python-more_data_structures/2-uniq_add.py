#!/usr/bin/python3
def uniq_add(my_list=[]):

    uni_element = []
    total = 0

    for element in my_list:
        if element not in uni_element:
            uni_element.append(element)
            total += element

    return total
