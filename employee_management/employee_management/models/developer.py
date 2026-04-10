from models.employee import Employee


class Developer(Employee):
    def __init__(self, employee_id, name, age, email, base_salary, programming_language, overtime_hours):
        super().__init__(employee_id, name, age, email, base_salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        overtime_pay = self.overtime_hours * 200000
        bonus = self.performance_score * 150000
        return self.base_salary + overtime_pay + bonus

    def display_info(self):
        return (
            super().display_info() +
            f"\nChức vụ: Developer"
            f"\nNgôn ngữ lập trình: {self.programming_language}"
            f"\nSố giờ OT: {self.overtime_hours}"
        )