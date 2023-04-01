#!/usr/bin/env python

# name    :	peeps.py
# version :	0.0.1
# date    :	20230329
# author  :	Leam Hall
# desc    :	Create a small number of NPCs for a 3d6 game

import argparse
import os
import random
import sqlite3
import sys


datadir    = 'data'
stat_names  = ['Str', 'Int', 'Wis', 'Dex', 'Con', 'Cha']


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


def gen_stats(roll = 3, keep = 3):
    """
    Generates 3d6 type stats, with optional modifiers
    """
    stats = {}
    for stat in stat_names:
        stats[stat] = roller(roll,6,keep) 
    return stats

def stat_mins(stats, mins):
    """
    Raises the base stats to the minimums provided in mins
    """
    for stat in mins.keys():
        stats[stat] = max(stats[stat], mins[stat])
    return stats

def  stat_maxs(stats, maxs):
    """
    Lowers the base stats to the maximums provided in maxs
    """
    for stat in maxs.keys():
        stats[stat] = min(stats[stat], maxs[stat])
    return stats
        

def start_family(data):
    """
    Takes the given data and builds a list of Peeps in the same family
    """
    family      = []
    father_age  = data.get('f_age', 16)
    mother_age  = data.get('m_age', father_age - 2)
    last_name   = data.get('l_name', get_name('last'))
    f_f_name    = data.get('f_f_name', get_name('male'))
    m_f_name    = data.get('m_f_name', get_name('female'))
    father      = peep_builder({'age': father_age, 'l_name': last_name, 'gender': 'm', 'f_name': f_f_name})
    mother      = peep_builder({'age': mother_age, 'l_name': last_name, 'gender': 'f', 'f_name': m_f_name})
    family.append(father)
    family.append(mother)
    kid_years   = time_for_kids(mother_age)
    kid_data    = { 'l_name': last_name }
    while kid_years > 0:
        kid_data['age'] = kid_years
        family.append(peep_child(kid_data))
        kid_data.pop('f_name', None)
        kid_data.pop('gender', None)
        kid_years -= random.randint(1,3)
    return family

def print_family(family):
    """
    Takes a list of family members, and prints each
    """
    print("Father: {}\n".format(family[0]))
    print("Mother: {}\n".format(family[1]))
    if len(family) > 2:
        for member in family[2:]:
            print("Child: {}\n".format(member))

def time_for_kids(m_age):
    """
    Returns an int of mother's age, minus 16, minus 1-3
    """
    return m_age - 16 - random.randint(1,3)

def peep_builder(data):
    """
    Generates the data and builds it into a Peep
    """
    young_child_max = { 'Str': 3, 'Wis': 3, 'Dex': 3 }
    older_child_max = { 'Str': 5, 'Wis': 5, 'Dex': 5 }
    data['stats']   = gen_stats()
    if data['age'] < 5:
        data['stats'] = stat_maxs(data['stats'], young_child_max)
    elif data['age'] < 12:
        data['stats'] = stat_maxs(data['stats'], older_child_max)
    data['gender']  = data.get('gender', random.choice(['m', 'f']))
    data['l_name']  = data.get('l_name', get_name('last'))
    if data['gender'] == 'f':
        data['f_name'] = data.get('f_name', get_name('female'))
    else:
        data['f_name'] = data.get('f_name', get_name('male'))

    return Peep(data)

def peep_child(data):
    """
    Generates a child, and modifies the stats
    """
    # needs to modify the stats

    child = peep_builder(data)
    
    return child

def peep_inserter(peep):
    """
    Inserts peep into DB
    """
    pass

def get_name(name):
    """
    Gets one random name (last, female, male) from a database
    """
    datafile    = 'names.db'
    datastore   = os.path.join(datadir, datafile)
    if not os.path.exists(datastore):
        raise FileNotFoundError
    if name == "male":
        table   = 'humaniti_male_first'
    elif name == "female":
        table   = 'humaniti_female_first'
    else:
        table   = 'humaniti_last'
    try:
        con     = sqlite3.connect(datastore)
    except Exception as e:
        print(e)
    cur         = con.cursor()
    result      = cur.execute("SELECT * from {} ORDER BY RANDOM() LIMIT 1".format(table))
    r           = result.fetchone()[0]
    cur.close()
    return r

    

def peep_init():
    """ 
    Creates the data dir and initializes the peep.db
    """
    datafile    = 'peeps.db'
    table       = 'peeps'
    datastore   = os.path.join(datadir, datafile)
    if not os.path.exists(datadir):
        os.makedirs(datadir) 
    con         = sqlite3.connect(datastore)
    cur         = con.cursor()
    cur.execute("DROP TABLE IF EXISTS {}".format(table))
    table       = """
                    CREATE TABLE peeps (
                        _id         INTEGER PRIMARY KEY ASC,
                        l_name      CHAR(25),
                        f_name      CHAR(25),
                        stat_str    INT,
                        stat_int    INT,
                        stat_wis    INT,
                        stat_dex    INT,
                        stat_con    INT,
                        stat_cha    INT,
                        gender      CHAR(1),
                        dob         INT,
                        spouse_id   INT,
                        father_id   INT,
                        mother_id   INT,
                        hit_points  INT,
                        village     CHAR(25)
                    );
                    """
    cur.execute(table)
    con.close()
 
    
class Peep:
    
    def __init__(self, data):
        self.stats = data.get('stats')
        self.l_name = data.get('l_name', 'Smith')
        self.f_name = data.get('f_name', 'Jim')
        self.age    = data.get('age', 16)
        self.gender = data.get('gender', 'f')

    def name(self):
        return "{} {}".format(self.f_name, self.l_name)

    def __str__(self):
        peep_string = "Name: {}  Age: {}\n".format(self.name(), self.age)
        results = [] 
        for stat in stat_names:
           results.append("{}: {:2d}".format(stat, self.stats[stat]) )
        peep_string +=  ", ".join(results)
        return peep_string
