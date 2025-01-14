import unittest
from flagger.flagger import (
    Flagger,
)
from flagger.exceptions import (
    TagNotFoundError,
    TypeNotFoundError,
    TypeMismatchError,
    OutOfBoundsArgs,
    InTestsError,
)


class BasicTypeTesting(unittest.TestCase):
    args: list = [
        "test.py",
        "-f",
        "10.3",
        "-i",
        "20",
        "-b",
        "True",
        "-s",
        "String",
        "-l",
        "1,2,3",
        "--flt",
        "10.3",
        "--int",
        "20",
        "--bool",
        "True",
        "--string",
        "String",
        "--list",
        "1.2.3",
    ]
    flagger: Flagger = Flagger(args=args)

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)

        self.parse_flag = self.flagger.parse_flag

    def test_short_int(self):
        self.assertIsInstance(self.parse_flag("-i", int), int)

    def test_short_float(self):
        self.assertIsInstance(self.parse_flag("-f", float), float)

    def test_short_str(self):
        self.assertIsInstance(self.parse_flag("-s", str), str)

    def test_short_bool(self):
        self.assertIsInstance(self.parse_flag("-b", bool), bool)

    def test_short_list(self):
        self.assertIsInstance(self.parse_flag("-l", list), list)

    def test_long_int(self):
        self.assertIsInstance(self.parse_flag("--int", int), int)

    def test_long_float(self):
        self.assertIsInstance(self.parse_flag("--flt", float), float)

    def test_long_str(self):
        self.assertIsInstance(self.parse_flag("--string", str), str)

    def test_long_bool(self):
        self.assertIsInstance(self.parse_flag("--bool", bool), bool)

    def test_long_list(self):
        self.assertIsInstance(self.parse_flag("--list", list, sep="."), list)


class BasicValueTesting(unittest.TestCase):
    args: list = [
        "test.py",
        "-f",
        "10.3",
        "-i",
        "20",
        "-b",
        "True",
        "-s",
        "String",
        "-l",
        "1,2,3",
        "--flt",
        "10.3",
        "--int",
        "20",
        "--bool",
        "True",
        "--string",
        "String",
        "--list",
        "1.2.3",
    ]
    flagger: Flagger = Flagger(args=args)

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)

        self.parse_flag = self.flagger.parse_flag

    def test_short_int(self):
        self.assertEqual(self.parse_flag("-i", int), 20)

    def test_short_float(self):
        self.assertEqual(self.parse_flag("-f", float), 10.3)

    def test_short_str(self):
        self.assertEqual(self.parse_flag("-s", str), "String")

    def test_short_bool(self):
        self.assertEqual(self.parse_flag("-b", bool), True)

    def test_short_list(self):
        self.assertEqual(self.parse_flag("-l", list), ["1", "2", "3"])

    def test_long_int(self):
        self.assertEqual(self.parse_flag("--int", int), 20)

    def test_long_float(self):
        self.assertEqual(self.parse_flag("--flt", float), 10.3)

    def test_long_str(self):
        self.assertEqual(self.parse_flag("--string", str), "String")

    def test_long_bool(self):
        self.assertEqual(self.parse_flag("--bool", bool), True)

    def test_long_list(self):
        self.assertEqual(
            self.flagger.parse_flag("--list", list, sep="."), ["1", "2", "3"]
        )


class ExistenceChecking(unittest.TestCase):
    args: list = ["test.py", "-f", "-long-flag"]
    flagger: Flagger = Flagger(args=args)

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)

        self.parse_flag = self.flagger.parse_flag

    def test_flag_in_args(self):
        self.assertEqual(self.parse_flag("-f"), True)

    def test_long_flag_in_args(self):
        self.assertEqual(self.parse_flag("-long-flag"), True)


class wrong_type:
    __name__ = "wrong"


class ExceptionTesting(unittest.TestCase):
    args: list = ["test.py", "-f", "10.3", "-i", "Text", "--int", "20", "--out"]
    flagger: Flagger = Flagger(args=args)

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)

        self.parse_flag = self.flagger.parse_flag

    def test_tag_not_found_error(self):
        try:
            self.assertEqual(self.parse_flag("-non-existent", int), 10)
        except TagNotFoundError:
            pass
        else:
            raise InTestsError("tag_not_found_error")

    def test_type_not_found_error(self):
        wrong = wrong_type()

        try:
            self.assertEqual(self.parse_flag("--int", wrong), 20)
        except TypeNotFoundError:
            pass
        else:
            raise InTestsError("type_not_found_error")

    def test_type_mismatch_error(self):
        try:
            self.assertEqual(self.parse_flag("-i", int), 10)
        except TypeMismatchError:
            pass
        else:
            raise InTestsError("type_mismatch_error")

    def test_out_of_bounds_args(self):
        try:
            self.assertEqual(self.parse_flag("--out", str), "test")
        except OutOfBoundsArgs:
            pass
        else:
            raise InTestsError("out_of_bounds_args")
