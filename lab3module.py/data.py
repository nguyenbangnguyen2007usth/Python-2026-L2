import math
import numpy as np
import UserInterface as ui

sinhvien = []
khoahoc = []
diemso = {}

def soluong_sinhvien():
    return ui.nhap_so_nguyen("nhap so luong sinh vien: ")

def thongtin_sinhvien():
    soluong = soluong_sinhvien()
    for i in range(soluong):
        msv = ui.nhap_so_nguyen("nhap ma sinh vien: ")
        hovaten = ui.c_input("nhap ho va ten sinh vien: ")
        DoB = ui.c_input("nhap ngay thang nam sinh: ")
        sinhvien.append({"msv": msv, "hovaten": hovaten, "DoB": DoB, "gpa": 0.0})

def soluong_khoahoc():
    return ui.nhap_so_nguyen("nhap so luong khoa hoc: ")

def thongtin_khoahoc():
    somonhoc = soluong_khoahoc()
    for i in range(somonhoc):
        masomonhoc = ui.nhap_so_nguyen("nhap ma so mon hoc (so): ")
        monhoc = ui.c_input("nhap mon hoc: ")
        tinchi = ui.nhap_so_nguyen("nhap so tin chi: ")
        khoahoc.append({"masomonhoc": masomonhoc, "monhoc": monhoc, "tinchi": tinchi})

def nhap_diemso():
    masomonhoc = ui.nhap_so_nguyen("nhap ma so mon hoc (so): ")
    diemso[masomonhoc] = {}
    ui.c_print(f"nhap diem cho khoa: {masomonhoc}")
    for sinhvien1 in sinhvien:
        diemmonhoc = float(ui.c_input(f"nhap diem cho {sinhvien1['hovaten']} (MSV: {sinhvien1['msv']}): "))
        diemso[masomonhoc][sinhvien1['msv']] = math.floor(diemmonhoc * 10) / 10.0

def danhsach_khoahoc():
    ui.c_print("\nDanh sach khoa hoc:")
    for khoahoc1 in khoahoc:
        ui.c_print(f"ID: {khoahoc1['masomonhoc']}, Ten: {khoahoc1['monhoc']}, Tin chi: {khoahoc1['tinchi']}")       

def danhsach_sinhvien():
    ui.c_print("\nDanh sach sinh vien:")
    for sinhvien1 in sinhvien:
        ui.c_print(f"MSV: {sinhvien1['msv']}, Ten: {sinhvien1['hovaten']}, Ngay sinh: {sinhvien1['DoB']}, GPA: {sinhvien1['gpa']:.1f}")

def choxemdiem_sinhvien():
    masomonhoc = ui.nhap_so_nguyen("\nnhap ma so mon hoc muon xem diem: ")
    if masomonhoc in diemso:
        ui.c_print(f"bang diem khoa hoc {masomonhoc}")
        for sinhvien1 in sinhvien:
            msv = sinhvien1['msv']
            if msv in diemso[masomonhoc]:
                ui.c_print(f"{sinhvien1['hovaten']} (MSV: {msv}): {diemso[masomonhoc][msv]}")
    else:
        ui.c_print("chua co diem cho mon hoc nay")

def tinh_gpa_va_sap_xep():
    """Hàm xử lý tính điểm trung bình và sắp xếp list sinh viên"""
    for sv in sinhvien:
        diem_list = []
        tinchi_list = []
        for kh in khoahoc:
            makh = kh['masomonhoc']
            if makh in diemso and sv['msv'] in diemso[makh]:
                diem_list.append(diemso[makh][sv['msv']])
                tinchi_list.append(kh['tinchi'])
        
        if len(diem_list) > 0:
            sv['gpa'] = np.average(np.array(diem_list), weights=np.array(tinchi_list))
    sinhvien.sort(key=lambda x: x['gpa'], reverse=True)