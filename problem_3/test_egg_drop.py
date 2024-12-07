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
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        solution_path = os.path.join(current_dir, 'solution.py')
        
        exec(open(solution_path).read())
        return fake_output.getvalue()
    return _run_solution

@pytest.mark.parametrize("input_data,expected_output,test_description", [
    (
        "3\n2 3 2",
        "4\n",
        "基本測試"
    ),
    (
        "4\n5 1 1 5",
        "10\n",
        "基本測試"
    )
])
def test_egg_drop(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output
