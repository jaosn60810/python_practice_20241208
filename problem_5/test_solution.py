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
    input_data = "1 2"
    expected_output = "16\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """零值測試"""
    input_data = "0 0"
    expected_output = "0\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """負數測試"""
    input_data = "-1 -2"
    expected_output = "-16\n"
    assert run_solution(input_data) == expected_output 