from abc import ABC, abstractmethod
from exceptions.employee_exceptions import (
    InvalidAgeError,
    InvalidSalaryError,
    ProjectAllocationError
)


class Employee(ABC):
    def __init__(self, employee_id, name, age, email, base_salary):
        if age < 18 or age > 65:
            raise InvalidAgeError("Tuổi phải nằm trong khoảng 18 đến 65")

        if base_salary <= 0:
            raise InvalidSalaryError("Lương cơ bản phải lớn hơn 0")

        if "@" not in email:
            raise ValueError("Email không hợp lệ")

        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.projects = []
        self.performance_score = 0

    def add_project(self, project_name):
        if len(self.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã có tối đa 5 dự án")
        self.projects.append(project_name)

    def remove_project(self, project_name):
        if project_name in self.projects:
            self.projects.remove(project_name)
        else:
            raise ValueError("Dự án không tồn tại trong danh sách")

    def update_performance(self, score):
        if score < 0 or score > 10:
            raise ValueError("Điểm hiệu suất phải từ 0 đến 10")
        self.performance_score = score

    def display_info(self):
        return (
            f"ID: {self.employee_id}\n"
            f"Tên: {self.name}\n"
            f"Tuổi: {self.age}\n"
            f"Email: {self.email}\n"
            f"Lương cơ bản: {self.base_salary}\n"
            f"Dự án: {', '.join(self.projects) if self.projects else 'Chưa có'}\n"
            f"Điểm hiệu suất: {self.performance_score}"
        )

    @abstractmethod
    def calculate_salary(self):
        pass