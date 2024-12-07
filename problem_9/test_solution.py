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
    input_data = "1 2 3 4 5 10 10 0 20 0 20"
    expected_output = "10\n10\n1\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """最小範圍測試"""
    input_data = "1 2 3 4 5 10 10 0 0 0 0"
    expected_output = "0\n0\n1\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """相同最大值，選擇較小的t"""
    input_data = "1 0 0 0 0 5 5 0 10 0 10"
    expected_output = "5\n5\n1\n"
    assert run_solution(input_data) == expected_output 