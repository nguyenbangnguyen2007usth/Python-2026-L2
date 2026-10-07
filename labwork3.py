import math
import numpy as np
import curses

stdscr = curses.initscr()
stdscr.scrollok(True)
curses.echo()

def _next_line():
    height, _ = stdscr.getmaxyx()
    y, _ = stdscr.getyx()
    if y >= height - 1:
        stdscr.scroll(1)
        y = height - 1
    else:
        y += 1
    stdscr.move(y, 0)

def _write_text(text):
    _, width = stdscr.getmaxyx()
    if width < 2:
        raise curses.error("Terminal is too narrow to display text")

    usable_width = width - 1
    y, x = stdscr.getyx()
    for index, line in enumerate(text.split("\n")):
        while line:
            if x >= usable_width:
                _next_line()
                y, x = stdscr.getyx()
            chunk = line[:usable_width - x]
            stdscr.addstr(y, x, chunk)
            x += len(chunk)
            line = line[len(chunk):]
        if index < text.count("\n"):
            _next_line()
            y, x = stdscr.getyx()

def print(*args):
    text = " ".join(map(str, args))
    _write_text(text + "\n")
    stdscr.refresh()

def input(prompt=""):
    _write_text(str(prompt))
    stdscr.refresh()
    return stdscr.getstr().decode()

def nhap_so_nguyen(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Vui long nhap mot so nguyen.")

sinhvien = []
khoahoc = []
diemso = {}

def soluong_sinhvien():
    return nhap_so_nguyen("nhap so luong sinh vien: ")

def thongtin_sinhvien():
    soluong = soluong_sinhvien()
    for i in range(soluong):
        msv = nhap_so_nguyen("nhap ma sinh vien: ")
        hovaten = input("nhap ho va ten sinh vien: ")
        DoB = input("nhap ngay thang nam sinh: ")
        sinhvien.append({"msv": msv, "hovaten": hovaten, "DoB": DoB, "gpa": 0.0})

def soluong_khoahoc():
    return nhap_so_nguyen("nhap so luong khoa hoc: ")

def thongtin_khoahoc():
    somonhoc = soluong_khoahoc()
    for i in range(somonhoc):
        masomonhoc = nhap_so_nguyen("nhap ma so mon hoc (so): ")
        monhoc = input("nhap mon hoc: ")
        tinchi = nhap_so_nguyen("nhap so tin chi: ")
        khoahoc.append({"masomonhoc": masomonhoc, "monhoc": monhoc, "tinchi": tinchi})

def nhap_diemso():
    masomonhoc = nhap_so_nguyen("nhap ma so mon hoc (so): ")
    diemso[masomonhoc] = {}
    print(f"nhap diem cho khoa: {masomonhoc}")
    for sinhvien1 in sinhvien:
        diemmonhoc = float(input(f"nhap diem cho {sinhvien1['hovaten']} (MSV: {sinhvien1['msv']}): "))
        diemso[masomonhoc][sinhvien1['msv']] = math.floor(diemmonhoc * 10) / 10.0

def danhsach_khoahoc():
    print("\nDanh sach khoa hoc:")
    for khoahoc1 in khoahoc:
        print(f"ID: {khoahoc1['masomonhoc']}, Ten: {khoahoc1['monhoc']}, Tin chi: {khoahoc1['tinchi']}")       

def danhsach_sinhvien():
    print("\nDanh sach sinh vien:")
    for sinhvien1 in sinhvien:
        print(f"MSV: {sinhvien1['msv']}, Ten: {sinhvien1['hovaten']}, Ngay sinh: {sinhvien1['DoB']}, GPA: {sinhvien1['gpa']:.1f}")

def choxemdiem_sinhvien():
    masomonhoc = nhap_so_nguyen("\nnhap ma so mon hoc muon xem diem: ")
    if masomonhoc in diemso:
        print(f"bang diem khoa hoc {masomonhoc}")
        for sinhvien1 in sinhvien:
            msv = sinhvien1['msv']
            if msv in diemso[masomonhoc]:
                print(f"{sinhvien1['hovaten']} (MSV: {msv}): {diemso[masomonhoc][msv]}")
    else:
        print("chua co diem cho mon hoc nay")

def lay_diem_gpa(x):
    return x['gpa']

# --- MAIN EXECUTION ---
stdscr.clear()
print("B1: NHAP THONG TIN SINH VIEN")
thongtin_sinhvien()

print("B2: NHAP THONG TIN KHOA HOC")
thongtin_khoahoc()

print("B3: NHAP DIEM")
nhap_diemso()
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

sinhvien.sort(key=lay_diem_gpa, reverse=True)

print("B4: HIEN THI DU LIEU")
danhsach_khoahoc()
danhsach_sinhvien()
choxemdiem_sinhvien()

print("\nNhan phim bat ky de thoat...")
curses.noecho()
stdscr.getch()
curses.endwin()