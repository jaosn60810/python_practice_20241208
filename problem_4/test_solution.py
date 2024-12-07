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
    input_data = "4\n1,1\n2,2\n3,3\n4,4"
    expected_output = "4\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """垂直線"""
    input_data = "3\n1,1\n1,2\n1,3"
    expected_output = "3\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """重複點"""
    input_data = "3\n1,1\n1,1\n2,2"
    expected_output = "2\n"
    assert run_solution(input_data) == expected_output 