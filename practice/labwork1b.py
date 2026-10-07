sinhvien = []
khoahoc = []
diemso = {}

def soluong_sinhvien():
    return int(input("nhap so luong sinh vien: "))
def thongtin_sinhvien():
    soluong = soluong_sinhvien()
    for i in range(soluong):
        msv = int(input("nhap ma sinh vien: "))
        hovaten = input("nhap ho va ten sinh vien: ")
        DoB = input("nhap ngay thang nam sinh: ")
        sinhvien.append({"msv": msv, "hovaten": hovaten, "DoB": DoB})
def soluong_khoahoc():
    return int(input("nhap so luong khoa hoc: "))
def thongtin_khoahoc():
    somonhoc = soluong_khoahoc()
    for i in range(somonhoc):
        masomonhoc = int(input("nhap ma so mon hoc: "))
        monhoc = input("nhap mon hoc: ")
        khoahoc.append({"masomonhoc": masomonhoc, "monhoc": monhoc})
def nhap_diemso():
    masomonhoc = int(input("nhap ma so mon hoc: "))
    diemso[masomonhoc] = {}
    print(f"nhap diem cho khoa: {masomonhoc}")
    for sinhvien1 in sinhvien:
        diemmonhoc = float(input(f"nhap diem cho {sinhvien1['hovaten']} (MSV: {sinhvien1['msv']}): "))
        diemso[masomonhoc][sinhvien1['msv']] = diemmonhoc
def danhsach_khoahoc():
    print("\nDanh sach khoa hoc:")
    for khoahoc1 in khoahoc:
        print(f"ID: {khoahoc1['masomonhoc']}, Ten: {khoahoc1['monhoc']}")       
def danhsach_sinhvien():
    print("\nDanh sach sinh vien:")
    for sinhvien1 in sinhvien:
        print(f"MSV: {sinhvien1['msv']}, Ten: {sinhvien1['hovaten']}, Ngay sinh: {sinhvien1['DoB']}")

def choxemdiem_sinhvien():
    masomonhoc = int(input("\nnhap ma so mon hoc muon xem diem: "))
    if masomonhoc in diemso:
        print(f"bang diem khoa hoc {masomonhoc}")
        for sinhvien1 in sinhvien:
            msv = sinhvien1['msv']
            if msv in diemso[masomonhoc]:
                print(f"{sinhvien1['hovaten']} (MSV: {msv}): {diemso[masomonhoc][msv]}")
    else:
        print("chua co diem cho mon hoc nay")

print("B1: NHAP THONG TIN SINH VIEN")
thongtin_sinhvien()
print("B2: NHAP THONG TIN KHOA HOC")
thongtin_khoahoc()
print("B3: NHAP DIEM")
nhap_diemso()
print("B4: HIEN THI DU LIEU")
danhsach_khoahoc()
danhsach_sinhvien()
choxemdiem_sinhvien()
