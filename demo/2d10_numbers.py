#!/usr/bin/env python

# name    :	2d10_numbers.py
# version :	0.0.1
# date    :	20230413
# author  :	Leam Hall
# desc    :	Show percentages of 2d10 rolls


def get_sum(number, keys, values):
    """
    int, list[int], list[int] => sum of slice
    returns the sum of values from index of number to the end of the list
    """
    if number > len(keys) + 1:
        return 0
    index = keys.index(number)
    return sum(values[index:])


def get_rolls():
    """
    None => list[int] list[int]
    returns keys and values of 2d10 rolls
    """
    rolls = {}
    keys = []
    values = []
    for i in range(1, 11):
        for j in range(1, 11):
            result = i + j
            if result not in rolls:
                rolls[result] = 1
            else:
                rolls[result] += 1
    for key, value in rolls.items():
        keys.append(key)
        values.append(value)
    return keys, values


keys, values = get_rolls()

for num in keys:
    print("{:2}:  {:3}".format(num, get_sum(num, keys, values)))
