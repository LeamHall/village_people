#!/usr/bin/env python

# name    :	combat_rolls.py
# version :	0.0.1
# date    :	20230408
# author  :	Leam Hall
# desc    :	Short combat roller for the VLC game.

## Notes
#  usage:
#   ./combat_rolls.py -f combatants.txt

import argparse
import random


class Combatant:
    DATA = [
        "name",
        "group",
        "str",
        "int",
        "wis",
        "dex",
        "con",
        "cha",
        "lvl",
        "hp",
        "ap",
        "skill",
        "wpn_dice",
    ]

    def __init__(self, data):
        stuff = data.split(":")
        for index, value in enumerate(self.DATA):
            setattr(self, value, stuff[index])
        self.current_hp = int(self.hp)

    def cbt_roll(self, mode="a"):
        modifier = 0
        if mode == "d":
            modifier = self.stat_mod("dex")
        return (
            random.randint(1, 10)
            + random.randint(1, 10)
            + int(self.skill)
            + modifier
        )

    def stat_mod(self, stat):
        mod = 0
        stat_value = getattr(self, stat)
        stat_value = int(stat_value)
        if stat_value == 18:
            mod = 3
        elif stat_value in range(16, 18):
            mod = 2
        elif stat_value in range(13, 16):
            mod = 1
        return mod

    def roll_damage(self):
        roll = self.stat_mod("str")
        for _ in range(0, int(self.wpn_dice)):
            roll += random.randint(1, 6)
        return roll

    def take_hit(self, dmg):
        self.current_hp -= dmg


def get_other_side(groups, peep):
    sides = list(groups.keys())
    sides.remove(peep.group)
    return sides[0]


def combat(peep, groups):
    damage = 0
    if not len(groups[peep.opponents]):
        return "{} has no one to attack. The fight is over.".format(peep.name)
    opponent = random.choice(groups[peep.opponents])
    atk = peep.cbt_roll()
    defense = opponent.cbt_roll("d")
    if atk >= defense:
        damage = peep.roll_damage() - int(opponent.ap) + peep.stat_mod("str")
    if atk > defense + 5:
        damage += atk - (defense + 5)
    result = "{} attacks {} with a {}, who defends with a {}".format(
        peep.name, opponent.name, atk, defense
    )
    if damage > 0:
        opponent.take_hit(damage)
        result += ". {} takes {} damage".format(opponent.name, damage)
        result += "\n{} is at {} hit points".format(
            opponent.name, opponent.current_hp
        )
        if opponent.current_hp <= 0:
            result += ". {} is dead".format(opponent.name)
            groups[peep.opponents].remove(opponent)
    result += "."
    return result


def list_from_file(file):
    data = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("#") or not len(line):
                continue
            data.append(line)
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f <file>",
        "--file",
        help="File to use for data",
        default="combatants.txt",
    )
    args = parser.parse_args()

    combatants = list_from_file(args.file)

    peeps = []
    groups = {}
    for c in combatants:
        peep = Combatant(c)
        if peep.group not in groups.keys():
            groups[peep.group] = []
        groups[peep.group].append(peep)

    in_combat = 1
    while in_combat:
        for group, peeps in groups.items():
            for p in peeps:
                p.opponents = get_other_side(groups, p)
                result = combat(p, groups)
                print(result)
                print("")
            if "over" in result:
                in_combat = 0
            continue
