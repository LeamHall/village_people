#!/usr/bin/env python

# name    :	make_peeps.py
# version :	0.0.2
# date    :	20240104
# author  :	Leam Hall
# desc    :	Create a small number of NPCs for a 3d6 game

"""
make_peeps.py creates a number of 3d6 OGL type fantasy characters.
"""

import argparse
import os
import random
import sqlite3
import sys


DATADIR                 = "data"
MAX_AGE                 = 80
MIN_CHILDBEARING_AGE    = 17
MAX_CHILDBEARING_AGE    = 30

stat_names = ["Str", "Int", "Wis", "Dex", "Con", "Cha"]

def child_age_range(m_age):
    """ Returns a max and min of potential children's ages. """
    if m_age < MIN_CHILDBEARING_AGE:
        oldest      = 0
        youngest    = 0
    else:
        oldest      = m_age - MIN_CHILDBEARING_AGE
        youngest    = max(1, m_age - MAX_CHILDBEARING_AGE)
    return oldest, youngest

def roller(num, die, keep=0):
    """
    Takes two positive integers, and an optional third.
    Returns a random int between keep and die * keep
    """
    num = int(num)
    die = int(die)
    keep = int(keep)
    if num < 0 or die < 0:
        print("Number of dice, and sides of dice, must be positive integer")
        return 0
    if keep < 0 or keep > num:
        keep = num
    rolls = []
    for _ in range(num):
        rolls.append(random.randint(1, die))
    rolls.sort()
    return sum(rolls[-keep:])


def gen_stats(roll=3, keep=3):
    """
    Generates 3d6 type stats, with optional modifiers
    """
    stats = {}
    for stat in stat_names:
        stats[stat] = roller(roll, 6, keep)
    return stats


def stat_mins(stats, mins):
    """
    Raises the base stats to the minimums provided in mins
    """
    for stat in mins.keys():
        stats[stat] = max(stats[stat], mins[stat])
    return stats


def stat_maxs(stats, maxs):
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
    family = []
    father_age = data.get("f_age", 16)
    mother_age = data.get("m_age", father_age - 2)
    last_name = data.get("l_name", get_name("last"))
    f_f_name = data.get("f_f_name", get_name("male"))
    m_f_name = data.get("m_f_name", get_name("female"))
    father = peep_builder(
        {
            "age": father_age,
            "l_name": last_name,
            "gender": "m",
            "f_name": f_f_name,
        }
    )
    mother = peep_builder(
        {
            "age": mother_age,
            "l_name": last_name,
            "gender": "f",
            "f_name": m_f_name,
        }
    )
    family.append(father)
    family.append(mother)

    max_kid_age, min_kid_age = child_age_range(mother_age)
    kid_data = {"l_name": last_name}
    while max_kid_age > min_kid_age:
        kid_data["age"] = max_kid_age
        family.append(peep_child(kid_data))
        kid_data.pop("f_name", None)
        kid_data.pop("gender", None)
        max_kid_age -= random.randint(1, 3)
    return family


def print_family(family):
    """
    Takes a list of family members, and prints each
    """
    print("Patron: {}\n".format(family[0]))
    print("Matron: {}\n".format(family[1]))
    if len(family) > 2:
        for member in family[2:]:
            print("  {}\n".format(member))


def peep_builder(data):
    """
    Generates the data and builds it into a Peep
    """
    young_child_max = {"Str": 3, "Wis": 3, "Dex": 3}
    older_child_max = {"Str": 5, "Wis": 5, "Dex": 5}
    data["stats"] = gen_stats()
    data["age"] = data.get("age", 16)
    if data["age"] < 5:
        data["stats"] = stat_maxs(data["stats"], young_child_max)
    elif data["age"] < 12:
        data["stats"] = stat_maxs(data["stats"], older_child_max)
    elif data["age"] > MAX_AGE:
        data["is_alive"] = False
    data["gender"] = data.get("gender", random.choice(["m", "f"]))
    data["l_name"] = data.get("l_name", get_name("last"))
    if data["gender"] == "f":
        data["f_name"] = data.get("f_name", get_name("female"))
    else:
        data["f_name"] = data.get("f_name", get_name("male"))

    return Peep(data)


def peep_child(data):
    """
    Generates a child, and modifies the stats
    """
    child = peep_builder(data)
    return child


def get_name(name_type):
    """
    Gets one random name (last, female, male) from a database
    """
    datafile = "names.db"
    datastore = os.path.join(DATADIR, datafile)
    if not os.path.exists(datastore):
        raise FileNotFoundError
    if name_type == "male":
        table = "humaniti_male_first"
    elif name_type == "female":
        table = "humaniti_female_first"
    else:
        table = "humaniti_last"
    try:
        con = sqlite3.connect(datastore)
    except Exception as e:
        print(e)
    cur = con.cursor()
    result = cur.execute(
        "SELECT * from {} ORDER BY RANDOM() LIMIT 1".format(table)
    )
    name = result.fetchone()[0]
    con.close()
    return name


def peep_init():
    """
    Creates the data dir and initializes the peep.db
    """
    datafile = "peeps.db"
    table = "peeps"
    datastore = os.path.join(DATADIR, datafile)
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR)
    con = sqlite3.connect(datastore)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS {}".format(table))
    table = """
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
    """
    Peep holds the data for a generated Peep.
    Peep.name() returns a string of first and last names.
    Peep.__str__() returns formatted Peep data.
    """

    def __init__(self, data):
        self.stats      = data.get("stats")
        self.l_name     = data.get("l_name", "Smith")
        self.f_name     = data.get("f_name", "Jim")
        self.age        = data.get("age", 16)
        self.gender     = data.get("gender", "f")
        self.is_alive   = data.get("is_alive", True)

    def name(self):
        """
        Return a string of f_name and l_name
        """
        return "{} {}".format(self.f_name, self.l_name)

    def __str__(self):
        peep_string = "{} [{}] Age: {}\n  ".format(
                self.name(), self.gender.upper(), self.age)
        if not self.is_alive:
            peep_string += "Deceased"
        else:
            results = []
            for stat in stat_names:
                results.append("{}: {:2d}".format(stat, self.stats[stat]))
            peep_string += ", ".join(results)
        return peep_string


if __name__ == "__main__":
    args = {}
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-i", "--init", action="store_true", help="Initialize data"
    )
    argparser.add_argument(
        "-f",
        "--family",
        action="store_true",
        default=False,
        help="Create a family",
    )
    argparser.add_argument(
        "--f-age", default=16, type=int, help="Age of the father, in years"
    )
    args = argparser.parse_args()

    if args.init:
        peep_init()
        sys.exit(0)
    elif args.family:
        input_data = {}
        if args.f_age > 14:
            input_data["f_age"] = args.f_age
        family = start_family(input_data)
        print_family(family)
    else:
        print(peep_builder({}))
