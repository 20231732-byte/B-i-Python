from models.employee import Employee


class Intern(Employee):
    def __init__(self, employee_id, name, age, email, base_salary, mentor, internship_duration):
        super().__init__(employee_id, name, age, email, base_salary)
        self.mentor = mentor
        self.internship_duration = internship_duration

    def calculate_salary(self):
        bonus = self.performance_score * 50000
        return self.base_salary + bonus

    def display_info(self):
        return (
            super().display_info() +
            f"\nChức vụ: Intern"
            f"\nMentor: {self.mentor}"
            f"\nThời gian thực tập: {self.internship_duration} tháng"
        )