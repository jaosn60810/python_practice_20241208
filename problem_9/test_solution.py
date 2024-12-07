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
        "1 2 3 4 5 10 10 0 20 0 20",
        "10\n10\n1\n",
        "基本測試"
    ),
    (
        "1 2 3 4 5 10 10 0 0 0 0",
        "0\n0\n1\n",
        "最小範圍測試"
    ),
    (
        "1 0 0 0 0 5 5 0 10 0 10",
        "5\n5\n1\n",
        "相同最大值，選擇較小的t"
    )
])
def test_solution(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output 