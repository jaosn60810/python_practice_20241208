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
        "3\nY P\nY O\nY Y",
        "1\n2\n0\n",
        "三種結果測試"
    ),
    (
        "5\nP P\nP Y\nY O\nP O\nO Y",
        "0\n2\n2\n1\n1\n",
        "多場次測試"
    )
])
def test_rock_paper_scissors(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output
