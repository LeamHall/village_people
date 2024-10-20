#!/usr/bin/env python

# name    :	make_peeps.py
# version :	0.0.2
# date    :	20240104
# author  :	Leam Hall
# desc    :	Create a small number of NPCs for a 3d6 game

"""
make_peeps.py creates a number of 3d6 (or other) OGL type fantasy characters.
"""

import argparse
import os
import os.path
import random
import sqlite3


DATADIR = "data"
MAX_AGE = 80
MIN_CHILDBEARING_AGE = 17
MAX_CHILDBEARING_AGE = 30

stat_names = [
    "Str",
    "Int",
    "Wis",
    "Dex",
    "Con",
    "Cha",
    "Siz",
    "Pow",
    "Soc",
    "App",
    "Edu",
]


def child_age_range(m_age):
    """Returns a max and min of potential children's ages."""
    if m_age < MIN_CHILDBEARING_AGE:
        oldest = 0
        youngest = 0
    else:
        oldest = m_age - MIN_CHILDBEARING_AGE
        youngest = max(1, m_age - MAX_CHILDBEARING_AGE)
    return oldest, youngest


def roller(num=1, die=6, keep=0, add=0):
    """
    Takes two positive integers, and an optional third and fourth.
    Returns a random int between keep and die * keep, plus add.
    """
    num = int(num)
    die = int(die)
    keep = int(keep)
    add = int(add)
    if num < 1:
        num = 1
    if die < 2:
        die = max(die, 6)
    if keep < 1 or keep > num:
        keep = num
    rolls = []
    for _ in range(num):
        rolls.append(random.randint(1, die))
    rolls.sort()
    return sum(rolls[-keep:]) + add


def gen_stats(roll=3, keep=3):
    """
    Generates 3d6 type stats, with optional modifiers
    """
    stats = {}
    for stat in stat_names:
        stats[stat] = roller(roll, 6, keep)
    stats["Siz"] = roller(2, 6, add=6)
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
    last_name = data.get("l_name", get_db_item("human_last"))
    f_f_name = data.get("f_f_name", get_db_item("human_male_first"))
    m_f_name = data.get("m_f_name", get_db_item("human_female_first"))
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


def write_family(family):
    """
    Takes a list of family members, and prints each
    """
    family_string = ""
    family_string += "Patron: {}\n".format(
        peep_to_template(family[0], args.game)
    )
    family_string += "Matron: {}\n".format(
        peep_to_template(family[1], args.game)
    )
    if len(family) > 2:
        for member in family[2:]:
            family_string += "{}\n".format(peep_to_template(member, args.game))
    return family_string


def peep_builder(data):
    """
    Generates the data and builds it into a Peep
    """
    young_child_max = {"Str": 3, "Wis": 3, "Dex": 3, "Siz": 3}
    older_child_max = {"Str": 5, "Wis": 5, "Dex": 5, "Siz": 8}
    data["stats"] = gen_stats()
    data["age"] = data.get("age", 16)
    if data["age"] < 5:
        data["stats"] = stat_maxs(data["stats"], young_child_max)
    elif data["age"] < 12:
        data["stats"] = stat_maxs(data["stats"], older_child_max)
    elif data["age"] > MAX_AGE:
        data["is_alive"] = False
    data["gender"] = data.get("gender", random.choice(["m", "f"]))
    data["l_name"] = data.get("l_name", get_db_item("human_last"))
    if data["gender"] == "f":
        data["f_name"] = data.get("f_name", get_db_item("human_female_first"))
    else:
        data["f_name"] = data.get("f_name", get_db_item("human_male_first"))
    data["temperament"] = data.get("temperament", get_db_item("temperaments"))
    data["plot"] = data.get("plot", get_db_item("plots"))
    data["negative_traits"] = data.get(
        "negative_traits", get_db_item("negative_traits")
    )
    data["positive_traits"] = data.get(
        "positive_traits", get_db_item("positive_traits")
    )
    return Peep(data)


def peep_child(data):
    """
    Generates a child, and modifies the stats
    """
    child = peep_builder(data)
    return child


def get_db_item(table):
    """
    Gets 1 random item from 'table'.
    """

    datafile = "build_village_peeps.db"
    datastore = os.path.join(DATADIR, datafile)
    if not os.path.exists(datastore):
        raise FileNotFoundError

    try:
        con = sqlite3.connect(datastore)
        cur = con.cursor()
        table_list = cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
        possible_tables = list()
        for tup in table_list.fetchall():
            possible_tables.append(tup[0])
    except Exception as e:
        print("EXCEPTION: ", e)

    if table not in possible_tables:
        raise ValueError(
            "Table {} not found, options are: {} ".format(
                table, ", ".join(possible_tables)
            )
        )

    result = cur.execute(
        "SELECT item from {} ORDER BY RANDOM() LIMIT 1".format(table)
    )
    item = result.fetchone()[0]
    con.close()
    return item


class Peep:
    """
    Peep holds the data for a generated Peep.
    Peep.name() returns a string of first and last names.
    Peep.__str__() returns formatted Peep data.
    """

    def __init__(self, data):
        self.stats = data.get("stats")
        self.l_name = data.get("l_name", "Smith")
        self.f_name = data.get("f_name", "Jim")
        self.age = data.get("age", 16)
        self.gender = data.get("gender", "f")
        self.is_alive = data.get("is_alive", True)
        self.plot = data.get("plot", "boring")
        self.temperament = data.get("temperament", "boring")
        self.negative_traits = data.get("negative_traits", "")
        self.positive_traits = data.get("positive_traits", "")

    def name(self):
        """
        Return a string of f_name and l_name
        """
        return "{} {}".format(self.f_name, self.l_name)


def pick_template(game):
    """Set the output template based on the game system used."""
    template = "{} [{}] Age: {:2}\n"
    if game == "brp":
        template += "Str: {:2} Con: {:2} Siz: {:2} Int: {:2} "
        template += "Pow: {:2} Dex: {:2} App: {:2} Edu: {:2}\n"
    else:
        template += (
            "Str: {:2} Int: {:2} Wis: {:2} Dex: {:2} Con: {:2} Cha: {:2}\n"
        )

    template += "Temperament: {}\n"
    template += "Plot: {}\n"
    template += "Positive Traits: {}\n"
    template += "Negative Traits: {}\n"

    return template


def rolled_stat_to_modifier(stat):
    """Convert a 3d6 roll to a basic -3 to +3 modifier for Hauberk."""
    modifier = 0
    if stat <= 3:
        modifier = -3
    elif stat in range(4, 5):
        modifier = -2
    elif stat in range(6, 7):
        modifier = -1
    elif stat in range(14, 15):
        modifier = 1
    elif stat in range(16, 17):
        modifier = 2
    elif stat >= 18:
        modifier = 3

    return modifier


def peep_to_template(peep, game):
    """Create the output string for the peep."""
    template = pick_template(game)
    peep_list = [peep.name(), peep.gender.upper(), peep.age]
    if game == "brp":
        peep_list += [peep.stats["Str"], peep.stats["Con"], peep.stats["Siz"]]
        peep_list += [peep.stats["Int"], peep.stats["Pow"], peep.stats["Dex"]]
        peep_list += [peep.stats["App"], peep.stats["Edu"]]
    elif game == "hauberk":
        peep_list += [
            rolled_stat_to_modifier(peep.stats["Str"]),
            rolled_stat_to_modifier(peep.stats["Int"]),
            rolled_stat_to_modifier(peep.stats["Wis"]),
            rolled_stat_to_modifier(peep.stats["Dex"]),
            rolled_stat_to_modifier(peep.stats["Con"]),
            rolled_stat_to_modifier(peep.stats["Cha"]),
        ]
    else:
        peep_list += [peep.stats["Str"], peep.stats["Int"], peep.stats["Wis"]]
        peep_list += [peep.stats["Dex"], peep.stats["Con"], peep.stats["Cha"]]
    peep_list += [
        peep.temperament,
        peep.plot,
        peep.positive_traits,
        peep.negative_traits,
    ]

    return template.format(*peep_list)


if __name__ == "__main__":
    args = {}
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-f",
        "--family",
        action="store_true",
        default=False,
        help="Create a family (default False)",
    )
    argparser.add_argument(
        "--f-age",
        default=16,
        type=int,
        help="Age of the father, in years (default 16)",
    )
    argparser.add_argument(
        "-g",
        "--game",
        default="adnd",
        type=str,
        help="Game system: adnd, brp, hauberk (default adnd)",
    )

    args = argparser.parse_args()

    args.game = args.game.lower()
    if args.game not in ["adnd", "brp", "hauberk"]:
        args.game = "adnd"
    if args.family:
        input_data = {}
        if args.f_age > 14:
            input_data["f_age"] = args.f_age
        family = start_family(input_data)
        family_data = write_family(family)
        print(family_data)
    else:
        peep = peep_builder({})
        peep_string = peep_to_template(peep, args.game)
        print(peep_string)
