# employee_manager/department.py
from typing import List
from .employee import Employee


class Department:
    """Represents a department of Employees"""

    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, emp: Employee) -> None:
        self.employees.append(emp)

    def avg_salary(self) -> float:
        if not self.employees:
            return 0.0
        return sum(e.salary for e in self.employees) / len(self.employees)
