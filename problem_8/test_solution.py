import pytest
from io import StringIO
from unittest.mock import patch

def run_solution(input_data):
    with patch('sys.stdin', StringIO(input_data)):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            exec(open('solution.py').read())
            return fake_output.getvalue()

def test_case1():
    """偶數且不被3整除"""
    input_data = "2\na"
    expected_output = "A\n"
    assert run_solution(input_data) == expected_output

def test_case2():
    """偶數且被3整除"""
    input_data = "6\na"
    expected_output = "a\n"
    assert run_solution(input_data) == expected_output

def test_case3():
    """奇數且被3整除"""
    input_data = "3\na"
    expected_output = "97\n"
    assert run_solution(input_data) == expected_output 