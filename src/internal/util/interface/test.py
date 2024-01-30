import unittest
from .implements import implements_interface

# Case 1: B class missing a method present in A
class A1:
    def method(self):
        pass

class B1_pass:
    def method(self):
        pass

class B1_fail:
    pass

# Case 3: B class missing a parameter in a method that exists in A
class A3:
    def method(self, param: int):
        pass

class B3_pass:
    def method(self, param: int):
        pass

class B3_fail:
    def method(self):
        pass

# Case 4: B class having an extra parameter in a method that is not in A
class A4:
    def method(self):
        pass

class B4_pass:
    def method(self):
        pass

class B4_fail:
    def method(self, param: int):
        pass

# Case 5: A parameter in a common method having different type hints in A and B
class A5:
    def method(self, param: int):
        pass

class B5_pass:
    def method(self, param: int):
        pass

class B5_fail:
    def method(self, param: str):
        pass

# Case 6: The return type of a common method having different type hints in A and B
class A6:
    def method(self) -> int:
        return 1

class B6_pass:
    def method(self) -> int:
        return 1

class B6_fail:
    def method(self) -> str:
        return "1"

# Case 7: Extra method in B
class A7:
    def method(self) -> int:
        return 1

class B7_pass:
    def method(self) -> int:
        return 1
    
    def method2(self) -> int:
        return 1


test_cases = [
    (A1, B1_pass, None),
    (A1, B1_fail, NotImplementedError),
    (A3, B3_pass, None),
    (A3, B3_fail, NotImplementedError),
    (A4, B4_pass, None),
    (A4, B4_fail, NotImplementedError),
    (A5, B5_pass, None),
    (A5, B5_fail, NotImplementedError),
    (A6, B6_pass, None),
    (A6, B6_fail, NotImplementedError),
    (A7, B7_pass, None),
]

class TestImplements(unittest.TestCase):
    def test_assert_implements_interface(self):
        for A, B, expected_exception in test_cases:
            if expected_exception:
                with self.assertRaises(expected_exception):
                    implements_interface(A, B)
            else:
                implements_interface(A, B)
            
            # test with instances
            
            if expected_exception:
                with self.assertRaises(expected_exception):
                    implements_interface(A(), B())
            else:
                implements_interface(A(), B())

if __name__ == '__main__':
    unittest.main()
