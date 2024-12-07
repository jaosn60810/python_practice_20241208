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
        "-2 1 -3 4 -1 2 1 -5 4",
        "子路徑為 4 -1 2 1 且最大能量和為 6\n",
        "基本測試"
    ),
    (
        "-1 -2 -3 -4",
        "子路徑為 -1 且最大能量和為 -1\n",
        "全負數"
    ),
    (
        "1 2 3 4",
        "子路徑為 1 2 3 4 且最大能量和為 10\n",
        "全正數"
    )
])
def test_solution(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output 