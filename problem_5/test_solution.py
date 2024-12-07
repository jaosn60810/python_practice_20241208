import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem5(unittest.TestCase):
    def test_case1(self):
        # 基本測試
        input_data = "1 2"
        expected_output = "16\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 零值測試
        input_data = "0 0"
        expected_output = "0\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 負數測試
        input_data = "-1 -2"
        expected_output = "-16\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 