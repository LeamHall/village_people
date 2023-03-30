#!/usr/bin/env python

# name    :	test/test_peeps.py
# version :	0.0.1
# date    :	20230329
# author  :	Leam Hall
# desc    :	Test the roller


import unittest

import peeps

class TestRoller(unittest.TestCase):

    def test_basic_roller(self):
        roll = peeps.roller(2, 10)
        self.assertTrue(roll >= 2 and roll <= 20)

    def test_min_and_max_roll(self):
        for x in range(1,100):
            roll = peeps.roller(3,6)
            self.assertTrue(roll >= 3 and roll <= 18)

    def test_keep(self):
        roll = peeps.roller(10,10,2)
        self.assertTrue(roll >= 2 and roll <= 20)

    def test_keep_min_and_max_roll(self):
        for x in range(1,100):
            roll = peeps.roller(30,6,3)
            self.assertTrue(roll >= 3 and roll <= 18)

class TestStats(unittest.TestCase):

    def test_basic_stats(self):
        stats = peeps.gen_stats()
        self.assertTrue(isinstance(stats, dict))

    def test_mins_stats(self):
        stats   = { 'Str': 10, 'Int': 1, 'Wis': 1, 'Con': 10, 'Cha': 5 }
        mins    = { 'Int': 10, 'Wis': 10, 'Cha': 10 }
        results = peeps.stat_mins(stats, mins)
        for stat in results.keys():
            self.assertTrue(results[stat] == 10)


class TestPeep(unittest.TestCase):

    def test_average_peep(self):
        data    = {}
        stats   = { 'Str': 10, 'Int': 10, 'Wis': 10, 'Dex': 9, 'Con': 10, 'Cha': 10 }
        data['stats'] = stats
        p       = peeps.Peep(data)
        expected = "Str: 10, Int: 10, Wis: 10, Dex:  9, Con: 10, Cha: 10"
        self.assertTrue(p.__str__() == expected)
