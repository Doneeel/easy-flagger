import unittest
from flagger.flagger import (
    Flagger,
)


class BasicTypeTesting(unittest.TestCase):
    args: list = ["test.py", '-f', '10.3', '-i', '20', '-b', 'True', '-s', 'String', '-l', '1,2,3',
                  '--flt', '10.3', '--int', '20', '--bool', 'True', '--string', 'String', '--list', '1.2.3']
    flagger: Flagger = Flagger(args=args)

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
        self.assertIsInstance(self.flagger.parse_flag(
            "--list", list, sep="."), list)


class BasicValueTesting(unittest.TestCase):
    args: list = ["test.py", '-f', '10.3', '-i', '20', '-b', 'True', '-s', 'String', '-l', '1,2,3',
                  '--flt', '10.3', '--int', '20', '--bool', 'True', '--string', 'String', '--list', '1.2.3']
    flagger: Flagger = Flagger(args=args)

    def test_short_int(self):
        self.assertEqual(self.flagger.parse_flag("-i", int), 20)

    def test_short_float(self):
        self.assertEqual(self.flagger.parse_flag("-f", float), 10.3)

    def test_short_str(self):
        self.assertEqual(self.flagger.parse_flag("-s", str), "String")

    def test_short_bool(self):
        self.assertEqual(self.flagger.parse_flag("-b", bool), True)

    def test_short_list(self):
        self.assertEqual(self.flagger.parse_flag("-l", list), ['1', '2', '3'])

    def test_long_int(self):
        self.assertEqual(self.flagger.parse_flag("--int", int), 20)

    def test_long_float(self):
        self.assertEqual(self.flagger.parse_flag("--flt", float), 10.3)

    def test_long_str(self):
        self.assertEqual(self.flagger.parse_flag("--string", str), "String")

    def test_long_bool(self):
        self.assertEqual(self.flagger.parse_flag("--bool", bool), True)

    def test_long_list(self):
        self.assertEqual(self.flagger.parse_flag(
            "--list", list, sep="."), ['1', '2', '3'])


class ExistenceChecking(unittest.TestCase):
    args: list = ["test.py", '-f', '-long-flag']
    flagger: Flagger = Flagger(args=args)

    def test_flag_in_args(self):
        self.assertEqual(self.flagger.parse_flag("-f"), True)

    def test_long_flag_in_args(self):
        self.assertEqual(self.flagger.parse_flag("-long-flag"), True)

    def test_flag_not_in_args(self):
        self.assertEqual(self.flagger.parse_flag("-n"), False)

    def test_long_flag_not_in_args(self):
        self.assertEqual(self.flagger.parse_flag("-non-existent-flag"), False)


# TODO : Testing for exceptions
class ExceptionTesting(unittest.TestCase):
    args: list = ["test.py", '-f', '10.3', '-i', 'Text', '-b', 'True', '-s', 'String', '-l', '1,2,3',
                  '--flt', '10.3', '--int', '20', '--bool', 'True', '--string', 'String', '--list', '1.2.3', '--out']
    flagger: Flagger = Flagger(args=args)
