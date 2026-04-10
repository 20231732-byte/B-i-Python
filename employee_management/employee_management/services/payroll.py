def calculate_employee_salary(employee):
    return employee.calculate_salary()


def calculate_total_company_salary(employees):
    return sum(employee.calculate_salary() for employee in employees)


def get_top_3_highest_salary(employees):
    sorted_employees = sorted(employees, key=lambda emp: emp.calculate_salary(), reverse=True)
    return sorted_employees[:3]