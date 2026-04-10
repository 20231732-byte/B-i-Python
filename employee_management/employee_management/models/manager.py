from models.employee import Employee


class Manager(Employee):
    def __init__(self, employee_id, name, age, email, base_salary, team_size, department):
        super().__init__(employee_id, name, age, email, base_salary)
        self.team_size = team_size
        self.department = department

    def calculate_salary(self):
        allowance = self.team_size * 500000
        bonus = self.performance_score * 100000
        return self.base_salary + allowance + bonus

    def display_info(self):
        return (
            super().display_info() +
            f"\nChức vụ: Manager"
            f"\nPhòng ban: {self.department}"
            f"\nSố thành viên nhóm: {self.team_size}"
        )