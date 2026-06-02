manager = []
next_id = 100 

while True:
    choice = int(input("""QUẢN LÝ NHÂN SỰ - STAFF MANAGER
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiếm nhân viên (theo mã)
4. Xóa nhân viên khỏi hệ thống
5. Thoát chương trình
Lựa chọn của bạn là: """))

    match choice:
        case 1:
            full_name = input("Tên của bạn là: ")
            if full_name.strip() == "":
                print("Tên nhân viên không được để trống")
                continue

            wage = float(input("Nhập vào mức lương của nhân viên: "))
            if wage < 0:
                print("Mức lương không hợp lệ")
                continue
            employee = {
                "id": next_id,
                "name": full_name,
                "salary": wage
            }
            manager.append(employee)
            print(f"Đã thêm nhân viên {full_name} với ID {next_id}")
            next_id += 1
        case 2:
            if manager == "":
                print("chưa có dữ liệu nhân sự")
            print(f"{'ID':<5}|{'TÊN NHÂN VIÊN':<25}|{'MỨC LƯƠNG':<10}")
            print(f"{employee['id']:<5}|{employee['name']:<25}|{employee['salary']:<10}")
        case 3:
            sreach_id = input("nhập vào id cần tìm kiếm: ")
            if not sreach_id == employee['id']:
                print("Không tìm thấy nhân viên có ID ",sreach_id)
            elif sreach_id == employee['id']:
                