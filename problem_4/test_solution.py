import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem4(unittest.TestCase):
    def test_case1(self):
        # 基本測試
        input_data = "4\n1,1\n2,2\n3,3\n4,4"
        expected_output = "4\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 垂直線
        input_data = "3\n1,1\n1,2\n1,3"
        expected_output = "3\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 重複點
        input_data = "3\n1,1\n1,1\n2,2"
        expected_output = "2\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 