import curses
import UserInterface as ui
import data
def main(stdscr):
    ui.init(stdscr)
    stdscr.clear()
    ui.c_print("B1: NHAP THONG TIN SINH VIEN")
    data.thongtin_sinhvien()
    ui.c_print("B2: NHAP THONG TIN KHOA HOC")
    data.thongtin_khoahoc()
    ui.c_print("B3: NHAP DIEM")
    data.nhap_diemso()
    data.tinh_gpa_va_sap_xep()
    ui.c_print("B4: HIEN THI DU LIEU")
    data.danhsach_khoahoc()
    data.danhsach_sinhvien()
    data.choxemdiem_sinhvien()
    ui.c_print("\nNhan phim bat ky de thoat...")
    curses.noecho()
    stdscr.getch()
if __name__ == "__main__":
    curses.wrapper(main)