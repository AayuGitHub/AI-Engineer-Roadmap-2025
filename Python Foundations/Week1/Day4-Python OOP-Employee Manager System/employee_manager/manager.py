import pandas as pd
from .employee import Employee
from .department import Department


class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.departments = {}

    def load_from_dataframe(self, df: pd.DataFrame):
        for _, row in df.iterrows():
            emp = Employee(
                emp_id=row["EmployeeNumber"],
                name=row["EmployeeNumber"],
                department=row["Department"],
                salary=row["MonthlyIncome"],
                attrition=row["Attrition"],
            )
            self.employees.append(emp)

            if emp.department not in self.departments:
                self.departments[emp.department] = Department(emp.department)

            self.departments[emp.department].add_employee(emp)

    def save_processed(self, path: str):
        data = [
            (e.emp_id, e.department, e.salary, e.attrition, e.annual_salary())
            for e in self.employees
        ]

        pd.DataFrame(
            data, columns=["ID", "Dept", "Salary", "Attrition", "AnnualSalary"]
        ).to_csv(path, index=False)
