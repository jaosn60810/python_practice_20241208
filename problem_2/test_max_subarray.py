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
        "1 2 3 4 5",
        "子路徑為 1 2 3 4 5 且最大能量和為 15\n",
        "全正數路徑"
    ),
    (
        "-1 -2 -3 -4 -5",
        "子路徑為 -1 且最大能量和為 -1\n",
        "全負數路徑"
    )
])
def test_max_subarray(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output


