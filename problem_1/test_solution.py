import pytest
from io import StringIO
from unittest.mock import patch

# Helper function to run solution with input and get output
def run_solution(input_data):
    with patch('sys.stdin', StringIO(input_data)):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            exec(open('solution.py').read())
            return fake_output.getvalue()

def test_case1():
    """基本測試：名字出現一次"""
    input_data = "顏成\n3\n林雅\n顏成\n小美"
    expected_output = "2\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """名字出現多次"""
    input_data = "顏成\n5\n顏成\n林雅\n顏成\n小美\n顏成"
    expected_output = "1\n3\n5\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """名字不存在"""
    input_data = "顏成\n3\n林雅\n小美\n大明"
    expected_output = "None\n"
    assert run_solution(input_data) == expected_output 