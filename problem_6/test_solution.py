import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem6(unittest.TestCase):
    def test_case1(self):
        # 基本測試
        input_data = "3\nY P\nP O\nO Y"
        expected_output = "1\n1\n1\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 平手測試
        input_data = "3\nY Y\nP P\nO O"
        expected_output = "0\n0\n0\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 玩家2獲勝
        input_data = "3\nP Y\nO P\nY O"
        expected_output = "2\n2\n2\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 