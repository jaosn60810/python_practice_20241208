import pytest
from io import StringIO
from unittest.mock import patch

def run_solution(input_data):
    with patch('sys.stdin', StringIO(input_data)):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            exec(open('solution.py').read())
            return fake_output.getvalue()

def test_case1():
    """基本測試"""
    input_data = "6\n5 1 6 10 3 2"
    expected_output = "19\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """只有一個蛋"""
    input_data = "1\n5"
    expected_output = "5\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """連續遞增"""
    input_data = "4\n1 2 3 4"
    expected_output = "6\n"
    assert run_solution(input_data) == expected_output 