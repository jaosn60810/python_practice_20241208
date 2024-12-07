import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem3(unittest.TestCase):
    def test_case1(self):
        # 基本測試
        input_data = "6\n5 1 6 10 3 2"
        expected_output = "19\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 只有一個蛋
        input_data = "1\n5"
        expected_output = "5\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 連續遞增
        input_data = "4\n1 2 3 4"
        expected_output = "6\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 