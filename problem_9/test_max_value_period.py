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
        "100 10 5 3 2 20 30 20 60 25 50",
        "22\n31\n461\n",
        "基本參數測試"
    ),
    (
        "223 31 17 3 5 37 19 20 60 10 52",
        "42\n21\n1787\n",
        "大數參數測試"
    )
])
def test_max_value_period(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output
