import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from employee_manager.employee import Employee


def test_annual_salary():
    e = Employee(1, "John Doe", "IT", 5000, "No")
    assert e.annual_salary() == 60000


def test_is_active():
    e = Employee(2, "Jane", "HR", 4000, "Yes")
    assert not e.is_active()
