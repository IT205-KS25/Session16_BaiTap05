'''
PHÂN TÍCH & THIẾT KẾ HỆ THỐNG

1. MỤC TIÊU HỆ THỐNG
- Quản lý danh sách bệnh nhân cấp cứu.
- Theo dõi sinh hiệu:
    + Nhịp tim (HR)
    + Nhiệt độ (TEMP)
- Cập nhật dữ liệu sinh hiệu nhanh chóng.
- Phát hiện bệnh nhân nguy kịch.
- Xóa hồ sơ khi xuất viện/chuyển khoa.
- Tối ưu xử lý dữ liệu bằng:
    + split()
    + join()
    + replace()
    + slicing
    + List xử lý chuỗi

2. CẤU TRÚC DỮ LIỆU

Mỗi bệnh nhân được lưu dưới dạng:
"ER01|Nguyen Van Quan|HR:115|TEMP:39.5"

Danh sách tổng:
er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5"
]

3. HELPER FUNCTIONS

--------------------------------------------------
Tên hàm:
find_patient_index(patients, er_id)

Input:
- patients (list)
- er_id (str)

Output:
- int

Mô tả xử lý:
- Duyệt danh sách bệnh nhân
- Dùng startswith(er_id)
- Nếu tìm thấy:
    return index
- Không tìm thấy:
    return -1
--------------------------------------------------

--------------------------------------------------
Tên hàm:
extract_vital_value(vital_string)

Input:
- vital_string (str)

Output:
- float

Mô tả xử lý:
- split(":")
- Lấy phần số phía sau
- Ép kiểu float

Ví dụ:
    "HR:115"
    ->
    115.0

    "TEMP:39.5"
    ->
    39.5
--------------------------------------------------

4. THIẾT KẾ HÀM

--------------------------------------------------
Tên hàm:
display_dashboard(patients)

Input:
- patients (list)

Output:
- None

Mô tả xử lý:
- Kiểm tra danh sách rỗng
- split("|") để tách dữ liệu
- Hiển thị bảng theo dõi
--------------------------------------------------

--------------------------------------------------
Tên hàm:
admit_patient(patients)

Input:
- patients (list)

Output:
- None

Mô tả xử lý:
- Nhập thông tin bệnh nhân
- Chuẩn hóa dữ liệu
- Kiểm tra:
    + mã ER rỗng
    + trùng mã
    + sinh hiệu hợp lệ
- Ghép dữ liệu bằng join()
- append() vào danh sách
--------------------------------------------------

--------------------------------------------------
Tên hàm:
update_vitals(patients)

Input:
- patients (list)

Output:
- None

Mô tả xử lý:
- Nhập mã ER
- Tìm bệnh nhân
- split("|")
- Chọn cập nhật:
    + HR
    + TEMP
- Sửa phần tử:
    index 2 hoặc 3
- join() tạo chuỗi mới
- Gán đè vào danh sách
--------------------------------------------------

--------------------------------------------------
Tên hàm:
trigger_red_alert(patients)

Input:
- patients (list)

Output:
- None

Mô tả xử lý:
- Duyệt danh sách
- Tách dữ liệu HR/TEMP
- extract_vital_value()
- Kiểm tra:
    + HR > 100
    + TEMP >= 39.0
- In danh sách nguy kịch
--------------------------------------------------

--------------------------------------------------
Tên hàm:
discharge_patient(patients)

Input:
- patients (list)

Output:
- None

Mô tả xử lý:
- Nhập mã ER
- Tìm index bệnh nhân
- pop() xóa khỏi danh sách
--------------------------------------------------

5. LUỒNG XỬ LÝ CHỨC NĂNG

CHỨC NĂNG 1
- Hiển thị dashboard bệnh nhân.

CHỨC NĂNG 2
- Tiếp nhận bệnh nhân mới.
- Chuẩn hóa dữ liệu.
- Kiểm tra lỗi dữ liệu.

CHỨC NĂNG 3
- Cập nhật lại sinh hiệu.
- split() -> sửa dữ liệu -> join().

CHỨC NĂNG 4
- Lọc bệnh nhân nguy kịch.
- So sánh HR và TEMP.

CHỨC NĂNG 5
- Xóa hồ sơ bệnh nhân.

CHỨC NĂNG 6
- Thoát chương trình.

6. EDGE CASES

- Trùng mã ER
- Mã ER rỗng
- Tên bệnh nhân rỗng
- Sinh hiệu nhập chữ
- TEMP <= 36.5
- Không tìm thấy mã ER
- Danh sách rỗng

7. KỸ THUẬT ĐÃ SỬ DỤNG

- split()
- join()
- replace()
- startswith()
- append()
- pop()
- title()
- upper()
- while True
- match-case
- Docstring
- snake_case
'''


"""
ER Triage System
- Emergency room patient management
- Track HR and TEMP
- Trigger red alert for critical patients
"""

# GLOBAL VARIABLES
er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]


# SPLIT FUNCTIONS
def split_patient(patient: str):
    """
    Tách dữ liệu bệnh nhân.

    Args:
        patient (str):
            Chuỗi bệnh nhân.

    Returns:
        list:
            Danh sách dữ liệu đã tách.
    """
    return patient.split("|")


def extract_vital_value(vital_string: str):
    """
    Lấy giá trị số từ chuỗi sinh hiệu.

    Args:
        vital_string (str):
            Chuỗi sinh hiệu.

    Returns:
        float:
            Giá trị sinh hiệu.
    """
    return float(vital_string.split(":")[1])


# FIND FUNCTIONS
def find_patient_index(patients: list, er_id: str):
    """
    Tìm vị trí bệnh nhân trong danh sách.

    Args:
        patients (list):
            Danh sách bệnh nhân.

        er_id (str):
            Mã ER.

    Returns:
        int:
            Index nếu tìm thấy,
            ngược lại trả về -1.
    """
    for index, patient in enumerate(patients):

        if patient.startswith(er_id):
            return index

    return -1


# NORMALIZE FUNCTIONS
def normalize_er_id(er_id: str):
    """
    Chuẩn hóa mã ER.

    Args:
        er_id (str):
            Mã ER.

    Returns:
        str:
            Mã ER đã chuẩn hóa.
    """
    return er_id.strip().upper()


def normalize_name(name: str):
    """
    Chuẩn hóa tên bệnh nhân.

    Args:
        name (str):
            Tên bệnh nhân.

    Returns:
        str:
            Tên đã chuẩn hóa.
    """
    return name.strip().title()


def create_hr_text(hr: str):
    """
    Tạo chuỗi HR.

    Args:
        hr (str):
            Nhịp tim.

    Returns:
        str:
            Chuỗi HR hoàn chỉnh.
    """
    return f"HR:{hr}"


def create_temp_text(temp: str):
    """
    Tạo chuỗi TEMP.

    Args:
        temp (str):
            Nhiệt độ.

    Returns:
        str:
            Chuỗi TEMP hoàn chỉnh.
    """
    return f"TEMP:{temp}"


# VALIDATION FUNCTIONS
def is_valid_number(value: str):
    """
    Kiểm tra dữ liệu số hợp lệ.

    Args:
        value (str):
            Giá trị cần kiểm tra.

    Returns:
        bool:
            True nếu hợp lệ,
            ngược lại False.
    """
    value = value.replace(".", "", 1)

    return value.isdigit()


def is_valid_hr(hr: str):
    """
    Kiểm tra nhịp tim hợp lệ.

    Args:
        hr (str):
            Nhịp tim.

    Returns:
        bool:
            True nếu hợp lệ,
            ngược lại False.
    """
    if not is_valid_number(hr):
        return False

    return float(hr) > 0


def is_valid_temp(temp: str):
    """
    Kiểm tra nhiệt độ hợp lệ.

    Args:
        temp (str):
            Nhiệt độ.

    Returns:
        bool:
            True nếu hợp lệ,
            ngược lại False.
    """
    if not is_valid_number(temp):
        return False

    return float(temp) >= 36.5


# DISPLAY FUNCTIONS
def display_dashboard(patients: list):
    """
    Hiển thị bảng theo dõi bệnh nhân.

    Args:
        patients (list):
            Danh sách bệnh nhân.

    Returns:
        None
    """
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ---------------------")

    for index, patient in enumerate(patients, 1):

        er_id, name, hr, temp = split_patient(patient)

        hr_value = extract_vital_value(hr)
        temp_value = extract_vital_value(temp)

        print(
            f"{index}. "
            f"[{er_id}] "
            f"{name:<20} | "
            f"Nhịp tim: {hr_value:.0f} bpm | "
            f"Nhiệt độ: {temp_value:.1f} °C"
        )

    print("--------------------------------------------------")


# ADMIT FUNCTIONS
def admit_patient(patients: list):
    """
    Tiếp nhận bệnh nhân mới.

    Args:
        patients (list):
            Danh sách bệnh nhân.

    Returns:
        None
    """
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ")
    er_id = normalize_er_id(er_id)

    if not er_id:
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("\nMã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = normalize_name(name)

    if not name:
        print("\nTên bệnh nhân không được để trống!")
        return

    while True:

        hr = input("Nhập nhịp tim HR: ")

        if is_valid_hr(hr):
            break

        print(
            "\nSinh hiệu không hợp lệ, "
            "vui lòng nhập số lớn hơn 0!"
        )

    while True:

        temp = input("Nhập nhiệt độ TEMP: ")

        if is_valid_temp(temp):
            break

        print(
            "Sinh hiệu không hợp lệ, "
            "vui lòng nhập số lớn hơn hoặc bằng 36.5!"
        )

    patient_data = [
        er_id,
        name,
        create_hr_text(hr),
        create_temp_text(temp)
    ]

    patient_record = "|".join(patient_data)

    patients.append(patient_record)

    print("\nTiếp nhận ca cấp cứu mới thành công!")

    print("Sau khi chuẩn hóa, dữ liệu được lưu là:")
    print(patient_record)


# UPDATE FUNCTIONS
def update_vitals(patients: list):
    """
    Cập nhật sinh hiệu bệnh nhân.

    Args:
        patients (list):
            Danh sách bệnh nhân.

    Returns:
        None
    """
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ")
    er_id = normalize_er_id(er_id)

    index = find_patient_index(patients, er_id)

    if index == -1:
        print(
            "Không tìm thấy bệnh nhân. "
            "Vui lòng kiểm tra lại mã ER!"
        )
        return

    patient_data = split_patient(patients[index])

    print(f"Tìm thấy bệnh nhân: {patient_data[1]}")

    print(
        f"Sinh hiệu hiện tại: "
        f"{patient_data[2]} | {patient_data[3]}"
    )

    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ")

    match choice:

        case "1":

            new_hr = input("Nhập nhịp tim mới: ")

            if not is_valid_hr(new_hr):

                print(
                    "\nSinh hiệu không hợp lệ, "
                    "vui lòng nhập số lớn hơn 0!"
                )

                return

            patient_data[2] = create_hr_text(new_hr)

            patients[index] = "|".join(patient_data)

            print("\nCập nhật nhịp tim thành công!")

        case "2":

            new_temp = input("Nhập nhiệt độ mới: ")

            if not is_valid_temp(new_temp):

                print(
                    "\nSinh hiệu không hợp lệ, "
                    "vui lòng nhập số lớn hơn hoặc bằng 36.5!"
                )

                return

            patient_data[3] = create_temp_text(new_temp)

            patients[index] = "|".join(patient_data)

            print("\nCập nhật nhiệt độ thành công!")

        case _:

            print(
                "\nLựa chọn không hợp lệ. "
                "Vui lòng chọn 1 hoặc 2!"
            )


# ALERT FUNCTIONS
def trigger_red_alert(patients: list):
    """
    Lọc bệnh nhân nguy kịch.

    Args:
        patients (list):
            Danh sách bệnh nhân.

    Returns:
        None
    """
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        return

    critical_patients = []

    for patient in patients:

        er_id, name, hr, temp = split_patient(patient)

        hr_value = extract_vital_value(hr)
        temp_value = extract_vital_value(temp)

        if hr_value > 100 or temp_value >= 39.0:

            critical_patients.append(
                (
                    er_id,
                    name,
                    hr_value,
                    temp_value
                )
            )

    if not critical_patients:

        print("\n--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")

        print(
            "Không có bệnh nhân nguy kịch "
            "tại thời điểm hiện tại."
        )

        return

    print(
        "\n!!! BÁO ĐỘNG ĐỎ - "
        "DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!"
    )

    for index, patient in enumerate(
        critical_patients,
        1
    ):

        er_id, name, hr, temp = patient

        print(
            f"{index}. "
            f"[{er_id}] "
            f"{name:<20} | "
            f"HR: {hr:.0f} bpm | "
            f"TEMP: {temp:.1f} °C | "
            f"CẦN XỬ LÝ KHẨN CẤP"
        )

    print("--------------------------------------------------")

    print(
        f"Tổng số ca nguy kịch: "
        f"{len(critical_patients)}"
    )


# DELETE FUNCTIONS
def discharge_patient(patients: list):
    """
    Xuất viện hoặc chuyển khoa.

    Args:
        patients (list):
            Danh sách bệnh nhân.

    Returns:
        None
    """
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input(
        "Nhập mã ER cần xóa khỏi hệ thống: "
    )

    er_id = normalize_er_id(er_id)

    if not er_id:
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:

        print(
            "Không tìm thấy bệnh nhân. "
            "Vui lòng kiểm tra lại mã ER!"
        )

        return

    patient_data = split_patient(
        patients.pop(index)
    )

    print(
        f"Đã chuyển khoa thành công cho "
        f"bệnh nhân {patient_data[1]}!"
    )


# MENU
while True:

    print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
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
            print(
                "Kết thúc ca trực. "
                "Hệ thống đã đóng!"
            )

            break

        case _:
            print("Lựa chọn không hợp lệ!")
