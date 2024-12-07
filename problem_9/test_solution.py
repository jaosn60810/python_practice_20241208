import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem9(unittest.TestCase):
    def test_case1(self):
        # 基本測試
        input_data = "1 2 3 4 5 10 10 0 20 0 20"
        expected_output = "10\n10\n1\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 最小範圍測試
        input_data = "1 2 3 4 5 10 10 0 0 0 0"
        expected_output = "0\n0\n1\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 相同最大值，選擇較小的t
        input_data = "1 0 0 0 0 5 5 0 10 0 10"
        expected_output = "5\n5\n1\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 