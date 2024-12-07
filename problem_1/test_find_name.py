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
        "Bob\n7\nAlice\nCantor\nDennis\nBob\nEric\nBob\nFrank",
        "4\n6\n",
        "名字出現多次"
    ),
    (
        "Mary\n4\nMARY\nmary\nMary0\n0Mary",
        "None\n",
        "名字不在名單中"
    )
])
def test_find_name(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output
