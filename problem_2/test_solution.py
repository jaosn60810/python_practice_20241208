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
    input_data = "-2 1 -3 4 -1 2 1 -5 4"
    expected_output = "子路徑為 4 -1 2 1 且最大能量和為 6\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """全負數"""
    input_data = "-1 -2 -3 -4"
    expected_output = "子路徑為 -1 且最大能量和為 -1\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """全正數"""
    input_data = "1 2 3 4"
    expected_output = "子路徑為 1 2 3 4 且最大能量和為 10\n"
    assert run_solution(input_data) == expected_output 