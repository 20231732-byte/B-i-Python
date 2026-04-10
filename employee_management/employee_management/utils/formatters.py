def format_employee_list(employees):
    if not employees:
        return "Chưa có dữ liệu"

    result = []
    for index, emp in enumerate(employees, start=1):
        result.append(f"\n--- Nhân viên {index} ---")
        result.append(emp.display_info())
        result.append(f"Lương thực nhận: {emp.calculate_salary()}")
    return "\n".join(result)