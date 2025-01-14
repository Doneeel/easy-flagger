import unittest
from flagger.flagger import (
    Flagger,
)
from flagger.exceptions import (
    TypeMismatchError,
    InTestsError,
)

class Elven:
    allowed = {
        "aerendyl": 1,
        "erendriel": 2,
        "galadriel": 3
    }
    
    @staticmethod
    def check(value: str):
        value = value.lower()
        is_allowed = value in Elven.allowed
        if not is_allowed:
            raise ValueError("the language is that of Mordor, which I will not utter here")
        
        return Elven.allowed.get(value) 


class Testing(unittest.TestCase):
    args: list = ["test.py", "-e1", "Aerendyl", "-e2", "Erendriel", "-e3", "Galadriel", "--not_e", "Ghorbash"]
    flagger: Flagger = Flagger(args=args)
    flagger.types.add_parser(Elven, Elven.check)

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        
        self.parse_flag = self.flagger.parse_flag

    def test_first_elf(self):
        self.assertEqual(self.parse_flag("-e1", Elven), 1)

    def test_second_elf(self):
        self.assertEqual(self.parse_flag("-e2", Elven), 2)
    
    def test_third_elf(self):
        self.assertEqual(self.parse_flag("-e3", Elven), 3)
    
    def test_orc(self):
        try:
            self.assertEqual(self.parse_flag("--not_e", Elven), 4)
        except TypeMismatchError:
            pass
        else:
            raise InTestsError("test_orc")
