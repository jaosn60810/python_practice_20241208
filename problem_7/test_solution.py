import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem7(unittest.TestCase):
    def test_case1(self):
        # 基本測試
        input_data = "2\nOOXOO\nOXOOO"
        expected_output = "7\n4\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 全對測試
        input_data = "1\nOOOO"
        expected_output = "10\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 全錯測試
        input_data = "1\nXXXX"
        expected_output = "0\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 