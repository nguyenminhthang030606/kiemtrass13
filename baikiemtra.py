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
            print(f"{manager['id']:<5}|{manager['name']:<25}|{manager['salary']:<10}")
        case 3:
            sreach_id = input("nhập vào id cần tìm kiếm: ")
            sreach = False
            for emp in manager:
                if emp == sreach_id:
                    print(f"{emp['id']} | {emp['name']} | {emp['salary']} ")
                    sreach = True
                    break
            if not sreach:
                print("không tìm thấy nhân viên")
        case 4:
            print()
        case 5:
            print("đã thoát ctrinh")
            break

