import pytest
from io import StringIO

@pytest.fixture
def run_solution(monkeypatch):
    def _run_solution(input_data):
        fake_input = StringIO(input_data)
        fake_output = StringIO()
        monkeypatch.setattr('sys.stdin', fake_input)
        monkeypatch.setattr('sys.stdout', fake_output)
        exec(open('solution.py').read())
        return fake_output.getvalue()
    return _run_solution

@pytest.mark.parametrize("input_data,expected_output,test_description", [
    (
        "2\na",
        "A\n",
        "偶數且不被3整除"
    ),
    (
        "6\na",
        "a\n",
        "偶數且被3整除"
    ),
    (
        "3\na",
        "97\n",
        "奇數且被3整除"
    )
])
def test_solution(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output 