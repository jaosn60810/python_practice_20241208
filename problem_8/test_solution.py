import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem8(unittest.TestCase):
    def test_case1(self):
        # 偶數且不被3整除
        input_data = "2\na"
        expected_output = "A\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 偶數且被3整除
        input_data = "6\na"
        expected_output = "a\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 奇數且被3整除
        input_data = "3\na"
        expected_output = "97\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 