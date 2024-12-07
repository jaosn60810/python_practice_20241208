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
        "1 2",
        "16\n",
        "基本測試"
    ),
    (
        "0 0",
        "0\n",
        "零值測試"
    ),
    (
        "-1 -2",
        "-16\n",
        "負數測試"
    )
])
def test_solution(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output 