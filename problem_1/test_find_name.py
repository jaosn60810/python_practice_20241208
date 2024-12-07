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
        "顏成\n3\n林雅\n顏成\n小美",
        "2\n",
        "基本測試：名字出現一次"
    ),
    (
        "顏成\n5\n顏成\n林雅\n顏成\n小美\n顏成",
        "1\n3\n5\n",
        "名字出現多次"
    ),
    (
        "顏成\n3\n林雅\n小美\n大明",
        "None\n",
        "名字不存在"
    )
])
def test_find_name(run_solution, input_data, expected_output, test_description):
    assert run_solution(input_data) == expected_output