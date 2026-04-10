from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError


def validate_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError("Tuổi phải nằm trong khoảng 18 đến 65")
    return age


def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lương phải lớn hơn 0")
    return salary


def validate_email(email):
    if "@" not in email:
        raise ValueError("Email không hợp lệ")
    return email


def validate_performance_score(score):
    if score < 0 or score > 10:
        raise ValueError("Điểm hiệu suất phải từ 0 đến 10")
    return score


def validate_menu_choice(choice, min_value, max_value):
    if choice < min_value or choice > max_value:
        raise ValueError(f"Vui lòng nhập số từ {min_value} đến {max_value}")
    return choice