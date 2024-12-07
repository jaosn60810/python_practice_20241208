import pytest
import os
from io import StringIO

@pytest.fixture
def run_solution(monkeypatch):
    def _run_solution(input_data):
        fake_input = StringIO(input_data)
        fake_output = StringIO()
        monkeypatch.setattr('sys.stdin', fake_input)
        monkeypatch.setattr('sys.stdout', fake_output)
        
        # Get the current test file's directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        solution_path = os.path.join(current_dir, 'solution.py')
        
        exec(open(solution_path).read())
        return fake_output.getvalue()
    return _run_solution

@pytest.mark.parametrize("input_data,expected_output,test_description", [
    (
        "3\nY P\nP O\nO Y",
        "1\n1\n1\n",
        "基本測試"
    ),
    (
        "3\nY Y\nP P\nO O",
        "0\n0\n0\n",
        "平手測試"
    ),
    (
        "3\nP Y\nO P\nY O",
        "2\n2\n2\n",
        "玩家2獲勝"
    )
])
def test_solution(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output 