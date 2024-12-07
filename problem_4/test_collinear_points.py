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
        "6\n1,1\n3,2\n5,3\n4,1\n2,3\n1,4",
        "4\n",
        "不同斜率測試"
    ),
    (
        "5\n1,1\n2,2\n3,3\n4,4\n2,2",
        "4\n",
        "重複點測試"
    )
])
def test_collinear_points(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output
