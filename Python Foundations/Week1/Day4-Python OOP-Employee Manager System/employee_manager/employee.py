# employee_manager/employee.py


class Employee:
    """Represents an employee."""

    def __init__(
        self, emp_id: int, name: str, department: str, salary: float, attrition: str
    ):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.attrition = attrition

    def annual_salary(self) -> float:
        """Return annual salary."""
        return self.salary * 12

    def is_active(self) -> bool:
        """Check if the employee has left"""
        return self.attrition.lower() == "no"
