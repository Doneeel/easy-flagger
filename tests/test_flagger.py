import unittest
from flagger.flagger import (
    Flagger,
)


class BasicTesting(unittest.TestCase):
    args: list = ["test.py", '-f', '10.3', '-i', '20', '-b', 'True', '-s', 'String', '-l', '1,2,3'
                , '--flt', '10.3', '--int', '20', '--bool', 'True', '--string', 'String', '--list', '1.2.3']
    flagger: Flagger = Flagger(args)

    def test_short_int(self):
        self.assertIsInstance(self.flagger.parse_flag("-i", int), int)
    def test_short_float(self):
        self.assertIsInstance(self.flagger.parse_flag("-f", float), float)
    def test_short_str(self):
        self.assertIsInstance(self.flagger.parse_flag("-s", str), str)
    def test_short_bool(self):
        self.assertIsInstance(self.flagger.parse_flag("-b", bool), bool)
    def test_short_list(self):
        self.assertIsInstance(self.flagger.parse_flag("-l", list), list)
    def test_long_int(self):
        self.assertIsInstance(self.flagger.parse_flag("--int", int), int)
    def test_long_float(self):
        self.assertIsInstance(self.flagger.parse_flag("--flt", float), float)
    def test_long_str(self):
        self.assertIsInstance(self.flagger.parse_flag("--string", str), str)
    def test_long_bool(self):
        self.assertIsInstance(self.flagger.parse_flag("--bool", bool), bool)
    def test_long_list(self):
        self.assertIsInstance(self.flagger.parse_flag("--list", list, sep="."), list)

# TODO : Testing for exceptions
class ExceptionTesting(unittest.TestCase):
    args: list = ["test.py", '-f', '10.3', '-i', 'Text', '-b', 'True', '-s', 'String', '-l', '1,2,3'
                , '--flt', '10.3', '--int', '20', '--bool', 'True', '--string', 'String', '--list', '1.2.3', '--out']
    flagger: Flagger = Flagger(args)
