#!/usr/bin/env python

# name    :	test/test_peeps.py
# version :	0.0.1
# date    :	20230329
# author  :	Leam Hall
# desc    :	Test the roller


import unittest

from peeps import peeps

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

    def test_stat_mins(self):
        stats   = { 'Str': 10, 'Int': 1, 'Wis': 1, 'Con': 10, 'Cha': 5 }
        mins    = { 'Int': 10, 'Wis': 10, 'Cha': 10 }
        results = peeps.stat_mins(stats, mins)
        for stat in results.keys():
            self.assertTrue(results[stat] == 10)

    def test_stat_maxs(self):
        stats   = { 'Str': 10, 'Int': 14, 'Wis': 21, 'Dex': 10, 'Con': 10, 'Cha': 5 }
        mins    = { 'Str': 2, 'Wis': 2, 'Dex': 2 }
        results = peeps.stat_maxs(stats, mins)
        for stat in mins.keys():
            self.assertTrue(results[stat] == 2)


class TestPeep(unittest.TestCase):

    def test_average_peep(self):
        data            = {}
        stats           = { 'Str': 10, 'Int': 10, 'Wis': 10, 'Dex': 9, 'Con': 10, 'Cha': 10 }
        data['stats']   = stats
        p               = peeps.Peep(data)
        expected        = "Str: 10, Int: 10, Wis: 10, Dex:  9, Con: 10, Cha: 10"
        self.assertTrue(expected in p.__str__())


class TestPeepBuilder(unittest.TestCase):

    def test_build_peep(self):
        data        = {"age": 16, "l_name": "Mythe", "gender": "m", "f_name": "George" }
        p           = peeps.peep_builder(data)
        expected    = "Str:"
        self.assertTrue(expected in p.__str__())
        self.assertTrue(p.age           == 16)
        self.assertTrue(type(p.stats)   == dict)
        self.assertTrue(p.name()        == "George Mythe")
        self.assertTrue(p.gender        == 'm')


class TestStartFamily(unittest.TestCase):
    
    def test_start_family(self):
        data    = {'f_age': 20, 'm_age': 18, 'l_name': 'Jones', 'f_f_name': "Mike", 'm_f_name': 'Susie'}
        family  = peeps.start_family(data)
        self.assertTrue(type(family) == list)
        self.assertTrue(len(family) >= 2)
        self.assertTrue(family[0].l_name == 'Jones')
        self.assertTrue(family[0].name() == "Mike Jones")
        self.assertTrue(family[0].age > family[1].age)


class TestPeepChild(unittest.TestCase):
    
    def test_base_child(self):
        data    = { 'l_name': "Garibaldi", 'age': 5 }
        c       = peeps.peep_child(data)
        self.assertTrue(c.l_name == 'Garibaldi')
        self.assertTrue(c.age == 5)

class TestGetName(unittest.TestCase):

    def test_last_name(self):
        last    = peeps.get_name('last')
        male    = peeps.get_name('male')
        female  = peeps.get_name('female')
        self.assertTrue(len(last)   >= 2)
        self.assertTrue(len(male)   >= 2)
        self.assertTrue(len(female) >= 2)
        
