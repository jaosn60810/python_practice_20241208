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
    input_data = "2\nOOXOO\nOXOOO"
    expected_output = "7\n4\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """全對測試"""
    input_data = "1\nOOOO"
    expected_output = "10\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """全錯測試"""
    input_data = "1\nXXXX"
    expected_output = "0\n"
    assert run_solution(input_data) == expected_output 