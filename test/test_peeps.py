#!/usr/bin/env python

# name    :	test/test_peeps.py
# version :	0.0.2
# date    :	20230329
# author  :	Leam Hall
# desc    :	Test all things peep

"""
test_peeps.py tests the make_peeps code.
"""

import unittest

import make_peeps as peeps


class TestRoller(unittest.TestCase):
    """TestRoller tests the roller method"""

    def test_basic_roller(self):
        """Test basic function of 2d10"""
        roll = peeps.roller(2, 10)
        self.assertTrue(roll in range(2, 21))

    def test_min_and_max_roll(self):
        """Run multiple tests to ensure numbers fall within the range"""
        for _ in range(1, 100):
            roll = peeps.roller(3, 6)
            self.assertTrue(roll in range(3, 19))

    def test_keep(self):
        """Test the ability to keep a limited number of dice"""
        roll = peeps.roller(10, 10, 2)
        self.assertTrue(roll in range(2, 21))

    def test_keep_min_and_max_roll(self):
        """Run multiple tests to ensure the kept dice stay within the range"""
        for _ in range(1, 100):
            roll = peeps.roller(30, 6, 3)
            self.assertTrue(roll in range(3, 19))


class TestStats(unittest.TestCase):
    """Checks the stat creation and alteration methods"""

    def test_basic_stats(self):
        """Verifies the result is a dict"""
        stats = peeps.gen_stats()
        self.assertTrue(isinstance(stats, dict))

    def test_stat_mins(self):
        """Verifies the alterations of minimums are met"""
        stats = {"Str": 10, "Int": 1, "Wis": 1, "Con": 10, "Cha": 5}
        mins = {"Int": 10, "Wis": 10, "Cha": 10}
        results = peeps.stat_mins(stats, mins)
        for stat in results.keys():
            self.assertTrue(results[stat] == 10)

    def test_stat_maxs(self):
        """Verifies the alterations of maximums are met"""
        stats = {
            "Str": 10,
            "Int": 14,
            "Wis": 21,
            "Dex": 10,
            "Con": 10,
            "Cha": 5,
        }
        mins = {"Str": 2, "Wis": 2, "Dex": 2}
        results = peeps.stat_maxs(stats, mins)
        for stat in mins.keys():
            self.assertTrue(results[stat] == 2)


class TestPeep(unittest.TestCase):
    """Test the Peep class"""

    def test_average_peep(self):
        """Verify that the stat data is used in Peep creation"""
        data = {}
        stats = {
            "Str": 10,
            "Int": 10,
            "Wis": 10,
            "Dex": 9,
            "Con": 10,
            "Cha": 10,
        }
        data["stats"] = stats
        peep = peeps.Peep(data)
        expected = "Str: 10, Int: 10, Wis: 10, Dex:  9, Con: 10, Cha: 10"
        self.assertTrue(expected in peep.__str__())


class TestPeepBuilder(unittest.TestCase):
    """Verifies peep_builder()"""

    def test_build_peep(self):
        """basic builder tests"""
        data = {
            "age":      16,
            "l_name":   "Mythe",
            "gender":   "m",
            "f_name":   "George",
            "is_alive": True,
        }
        peep = peeps.peep_builder(data)
        expected = "Str:"
        self.assertTrue(expected in peep.__str__())
        self.assertTrue(peep.age == 16)
        self.assertTrue(peep.name() == "George Mythe")
        self.assertTrue(peep.gender == "m")
        self.assertTrue(peep.is_alive)

    def test_build_old_peep(self):
        """basic builder tests"""
        data = {
            "age":      86,
            "l_name":   "Mythe",
            "gender":   "m",
            "f_name":   "George",
        }
        peep = peeps.peep_builder(data)
        self.assertTrue(peep.age == 86)
        self.assertFalse(peep.is_alive)
        self.assertTrue("Deceased" in peep.__str__())


    def test_build_defaults(self):
        """Tests the default settings of the builder"""
        data = {}
        peep = peeps.peep_builder(data)
        self.assertTrue(peep.age == 16)
        self.assertTrue(peep.gender in ["m", "f"])
        self.assertTrue(peep.is_alive)
        self.assertTrue(isinstance(peep.stats, dict))
        self.assertTrue("Str" in peep.stats)


class TestStartFamily(unittest.TestCase):
    """Verifies start_family()"""

    def test_start_family(self):
        """Verifies at least two members in the family"""
        data = {
            "f_age": 20,
            "m_age": 18,
            "l_name": "Jones",
            "f_f_name": "Mike",
            "m_f_name": "Susie",
        }
        family = peeps.start_family(data)
        self.assertTrue(isinstance(family, list))
        self.assertTrue(len(family) >= 2)
        self.assertTrue(family[0].l_name == "Jones")
        self.assertTrue(family[0].name() == "Mike Jones")
        self.assertTrue(family[0].age > family[1].age)


class TestPeepChild(unittest.TestCase):
    """Ensures the child meets expectations"""

    def test_base_child(self):
        """Check the initial creation, given data"""
        data = {"l_name": "Garibaldi", "age": 5}
        child = peeps.peep_child(data)
        self.assertTrue(child.l_name == "Garibaldi")
        self.assertTrue(child.age == 5)


class TestGetName(unittest.TestCase):
    """Checks all of the get_name() functionality"""

    def test_last_name(self):
        """Ensure the name isn't an empty string"""

        last = peeps.get_name("last")
        male = peeps.get_name("male")
        female = peeps.get_name("female")
        self.assertTrue(len(last) >= 2)
        self.assertTrue(len(male) >= 2)
        self.assertTrue(len(female) >= 2)
