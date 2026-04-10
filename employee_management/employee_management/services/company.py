from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    DuplicateEmployeeError
)


class Company:
    def __init__(self):
        self.employees = []

    def generate_new_id(self):
        if not self.employees:
            return "EMP001"

        numbers = []
        for emp in self.employees:
            if emp.employee_id.startswith("EMP"):
                try:
                    numbers.append(int(emp.employee_id[3:]))
                except ValueError:
                    continue

        if not numbers:
            return "EMP001"

        max_id = max(numbers)
        return f"EMP{max_id + 1:03d}"

    def add_employee(self, employee):
        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                raise DuplicateEmployeeError(f"Trùng mã nhân viên: {employee.employee_id}")
        self.employees.append(employee)

    def add_employee_auto_id(self, employee_type, name, age, email, base_salary, *args):
        new_id = self.generate_new_id()

        if employee_type.lower() == "manager":
            employee = Manager(new_id, name, age, email, base_salary, *args)
        elif employee_type.lower() == "developer":
            employee = Developer(new_id, name, age, email, base_salary, *args)
        elif employee_type.lower() == "intern":
            employee = Intern(new_id, name, age, email, base_salary, *args)
        else:
            raise ValueError("Loại nhân viên không hợp lệ")

        self.employees.append(employee)
        return employee

    def get_all_employees(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        return self.employees

    def find_employee_by_id(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        raise EmployeeNotFoundError(employee_id)

    def find_employee_by_name(self, keyword):
        result = []
        for emp in self.employees:
            if keyword.lower() in emp.name.lower():
                result.append(emp)

        if not result:
            raise EmployeeNotFoundError(f"Tên chứa '{keyword}'")
        return result

    def delete_employee(self, employee_id):
        employee = self.find_employee_by_id(employee_id)
        self.employees.remove(employee)

    def update_employee_email(self, employee_id, new_email):
        employee = self.find_employee_by_id(employee_id)
        if "@" not in new_email:
            raise ValueError("Email không hợp lệ")
        employee.email = new_email

    def assign_project_to_employee(self, employee_id, project_name):
        employee = self.find_employee_by_id(employee_id)
        employee.add_project(project_name)

    def remove_project_from_employee(self, employee_id, project_name):
        employee = self.find_employee_by_id(employee_id)
        employee.remove_project(project_name)

    def update_employee_performance(self, employee_id, score):
        employee = self.find_employee_by_id(employee_id)
        employee.update_performance(score)

    def get_excellent_employees(self):
        return [emp for emp in self.employees if emp.performance_score > 8]

    def get_low_performance_employees(self):
        return [emp for emp in self.employees if emp.performance_score < 5]

    def filter_by_type(self, employee_type):
        result = []
        for emp in self.employees:
            if emp.__class__.__name__.lower() == employee_type.lower():
                result.append(emp)
        return result

    def sort_by_performance_desc(self):
        return sorted(self.employees, key=lambda emp: emp.performance_score, reverse=True)

    def get_total_employees(self):
        return len(self.employees)

    def get_salary_summary(self):
        total_salary = sum(emp.calculate_salary() for emp in self.employees)
        average_salary = total_salary / len(self.employees) if self.employees else 0
        return total_salary, average_salary