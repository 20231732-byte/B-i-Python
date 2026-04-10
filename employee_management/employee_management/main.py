from services.company import Company
from services.payroll import (
    calculate_employee_salary,
    calculate_total_company_salary,
    get_top_3_highest_salary
)
from utils.formatters import format_employee_list


def show_menu():
    print("\n========== HỆ THỐNG QUẢN LÝ NHÂN VIÊN ==========")
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách nhân viên")
    print("3. Tìm nhân viên theo ID")
    print("4. Tính lương từng nhân viên")
    print("5. Tính tổng lương công ty")
    print("6. Top 3 nhân viên lương cao nhất")
    print("7. Phân công dự án")
    print("8. Cập nhật điểm hiệu suất")
    print("9. Hiển thị nhân viên xuất sắc")
    print("10. Hiển thị nhân viên cần cải thiện")
    print("11. Xóa nhân viên")
    print("0. Thoát")


def add_employee_menu(company):
    print("\n--- Chọn loại nhân viên ---")
    print("1. Manager")
    print("2. Developer")
    print("3. Intern")

    choice = int(input("Nhập lựa chọn: "))

    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    email = input("Nhập email: ")
    base_salary = float(input("Nhập lương cơ bản: "))

    if choice == 1:
        team_size = int(input("Nhập số thành viên nhóm: "))
        department = input("Nhập phòng ban: ")
        employee = company.add_employee_auto_id(
            "manager", name, age, email, base_salary, team_size, department
        )
    elif choice == 2:
        programming_language = input("Nhập ngôn ngữ lập trình: ")
        overtime_hours = int(input("Nhập số giờ OT: "))
        employee = company.add_employee_auto_id(
            "developer", name, age, email, base_salary, programming_language, overtime_hours
        )
    elif choice == 3:
        mentor = input("Nhập tên mentor: ")
        internship_duration = int(input("Nhập thời gian thực tập (tháng): "))
        employee = company.add_employee_auto_id(
            "intern", name, age, email, base_salary, mentor, internship_duration
        )
    else:
        print("Lựa chọn không hợp lệ")
        return

    print(f"Đã thêm nhân viên thành công với mã: {employee.employee_id}")


def main():
    company = Company()

    while True:
        try:
            show_menu()
            choice = int(input("Nhập lựa chọn của bạn: "))

            if choice == 1:
                add_employee_menu(company)

            elif choice == 2:
                employees = company.get_all_employees()
                print(format_employee_list(employees))

            elif choice == 3:
                employee_id = input("Nhập ID nhân viên cần tìm: ")
                employee = company.find_employee_by_id(employee_id)
                print(employee.display_info())
                print(f"Lương thực nhận: {employee.calculate_salary()}")

            elif choice == 4:
                employees = company.get_all_employees()
                for emp in employees:
                    print(f"{emp.name} ({emp.employee_id}) - Lương: {calculate_employee_salary(emp)}")

            elif choice == 5:
                employees = company.get_all_employees()
                total_salary = calculate_total_company_salary(employees)
                print(f"Tổng lương công ty: {total_salary}")

            elif choice == 6:
                employees = company.get_all_employees()
                top3 = get_top_3_highest_salary(employees)
                print("\n--- Top 3 nhân viên lương cao nhất ---")
                for emp in top3:
                    print(f"{emp.name} ({emp.employee_id}) - Lương: {emp.calculate_salary()}")

            elif choice == 7:
                employee_id = input("Nhập ID nhân viên: ")
                project_name = input("Nhập tên dự án: ")
                company.assign_project_to_employee(employee_id, project_name)
                print("Phân công dự án thành công")

            elif choice == 8:
                employee_id = input("Nhập ID nhân viên: ")
                score = float(input("Nhập điểm hiệu suất (0-10): "))
                company.update_employee_performance(employee_id, score)
                print("Cập nhật điểm hiệu suất thành công")

            elif choice == 9:
                excellent = company.get_excellent_employees()
                print(format_employee_list(excellent))

            elif choice == 10:
                low_perf = company.get_low_performance_employees()
                print(format_employee_list(low_perf))

            elif choice == 11:
                employee_id = input("Nhập ID nhân viên cần xóa: ")
                company.delete_employee(employee_id)
                print("Xóa nhân viên thành công")

            elif choice == 0:
                print("Thoát chương trình.")
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại")

        except Exception as e:
            print(f"Lỗi: {e}")


if __name__ == "__main__":
    main()