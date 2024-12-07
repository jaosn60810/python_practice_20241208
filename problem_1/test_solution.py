import unittest
from io import StringIO
from unittest.mock import patch
from solution import *

class TestProblem1(unittest.TestCase):
    def test_case1(self):
        # 基本測試：名字出現一次
        input_data = "顏成\n3\n林雅\n顏成\n小美"
        expected_output = "2\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case2(self):
        # 名字出現多次
        input_data = "顏成\n5\n顏成\n林雅\n顏成\n小美\n顏成"
        expected_output = "1\n3\n5\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_case3(self):
        # 名字不存在
        input_data = "顏成\n3\n林雅\n小美\n大明"
        expected_output = "None\n"
        with patch('sys.stdin', StringIO(input_data)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                exec(open('solution.py').read())
                self.assertEqual(fake_output.getvalue(), expected_output) 