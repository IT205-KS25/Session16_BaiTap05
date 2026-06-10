er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]


def find_patient_index(patients, er_id):
    er_id = er_id.strip().upper()

    for index, patient in enumerate(patients):
        if patient.startswith(er_id + "|"):
            return index

    return -1


def extract_vital_value(vital_string):
    return float(vital_string.split(":")[1])


def input_hr():
    while True:
        hr = input("Nhập nhịp tim HR: ").strip()

        if hr.isdigit() and int(hr) > 0:
            return hr

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")


def input_temp():
    while True:
        temp = input("Nhập nhiệt độ TEMP: ").strip()

        if temp.replace(".", "", 1).isdigit() and float(temp) >= 36.5:
            return temp

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")


def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")

    for index, patient in enumerate(patients, start=1):
        er_id, name, hr, temp = patient.split("|")

        print(
            f"{index}. [{er_id}] {name:<18} | Nhịp tim: {hr.split(':')[1]} bpm | Nhiệt độ: {temp.split(':')[1]} °C"
        )

    print("-----------------------------------------------------------------")


def admit_patient(patients):
    print("--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()

    if er_id == "":
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()

    if name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    hr = input_hr()
    temp = input_temp()

    name = name.title()

    record = "|".join([
        er_id,
        name,
        f"HR:{hr}",
        f"TEMP:{temp}"
    ])

    patients.append(record)

    print("\nTiếp nhận ca cấp cứu mới thành công!")
    print(record)


def update_vitals(patients):
    print("--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    data = patients[index].split("|")

    print(f"Tìm thấy bệnh nhân: {data[1]}")
    print(f"Sinh hiệu hiện tại: {data[2]} | {data[3]}")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ")

    if choice == "1":
        while True:
            value = input("Nhập nhịp tim mới: ").strip()

            if value.isdigit() and int(value) > 0:
                data[2] = f"HR:{value}"
                patients[index] = "|".join(data)

                print("\nCập nhật nhịp tim thành công!")
                break

            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    elif choice == "2":
        while True:
            value = input("Nhập nhiệt độ mới: ").strip()

            if value.replace(".", "", 1).isdigit() and float(value) >= 36.5:
                data[3] = f"TEMP:{value}"
                patients[index] = "|".join(data)

                print("\nCập nhật nhiệt độ thành công!")
                break

            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")


def trigger_red_alert(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    critical_cases = []

    for patient in patients:
        data = patient.split("|")

        hr = extract_vital_value(data[2])
        temp = extract_vital_value(data[3])

        if hr > 100 or temp >= 39:
            critical_cases.append(patient)

    if len(critical_cases) == 0:
        print("--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
        return

    print("!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")

    for index, patient in enumerate(critical_cases, start=1):
        er_id, name, hr, temp = patient.split("|")

        print(
            f"{index}. [{er_id}] {name} | HR: {hr.split(':')[1]} bpm | TEMP: {temp.split(':')[1]} °C | CẦN XỬ LÝ KHẨN CẤP"
        )

    print("-----------------------------------------------------")
    print(f"Tổng số ca nguy kịch: {len(critical_cases)}")


def discharge_patient(patients):
    print("--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()

    if er_id == "":
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    name = patients[index].split("|")[1]

    patients.pop(index)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {name}!")


while True:
    print()
    print("===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
    print("1. Bảng theo dõi bệnh nhân")
    print("2. Tiếp nhận ca cấp cứu mới")
    print("3. Cập nhật lại sinh hiệu")
    print("4. BÁO ĐỘNG ĐỎ Lọc bệnh nhân nguy kịch")
    print("5. Xuất viện / Chuyển khoa")
    print("6. Thoát chương trình")
    print("=================================================")

    choice = input("Chọn chức năng (1-6): ")

    match choice:
        case "1":
            display_dashboard(er_patients)

        case "2":
            admit_patient(er_patients)

        case "3":
            update_vitals(er_patients)

        case "4":
            trigger_red_alert(er_patients)

        case "5":
            discharge_patient(er_patients)

        case "6":
            print("Kết thúc ca trực. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-6!")