#!/usr/bin/env python

# name    :	peeps.py
# version :	0.0.1
# date    :	20230329
# author  :	Leam Hall
# desc    :	Create a small number of NPCs for a 3d6 game

import random

stat_names = ['Str', 'Int', 'Wis', 'Dex', 'Con', 'Cha']


def roller(num, die, keep = 0):
    """ 
    roller takes two positive integers, and an optional third. 
    Returns a random int between keep and die * keep 
    """
    num     = int(num)
    die     = int(die)
    keep    = int(keep)
    if num < 0 or die < 0:
        print("Number of dice, and sides of dice, must be positive integer")
        return 0
    if keep < 0 or keep > num:
        keep = num
    rolls     = []
    for i in range(num):
        rolls.append(random.randint(1,die))
    rolls.sort()
    return sum(rolls[-keep:]) 


def gen_stats():
    """
    Generates 3d6 type stats, with optional modifiers
    """
    stats = {}
    for stat in stat_names:
        stats[stat] = roller(3,6) 
    return stats

def stat_mins(stats, mins):
    """
    Raises the base stats to the minimums provided in mins
    """
    for stat in mins.keys():
        stats[stat] = max(stats[stat], mins[stat])
    return stats

class Peep:

    def __init__(self, data):
        self.stats = data.get('stats')

    def __str__(self):
        results = [] 
        for stat in stat_names:
           results.append("{}: {:2d}".format(stat, self.stats[stat]) )
        return ", ".join(results)

#####
#for x in range(1,6):
    
