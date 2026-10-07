import curses

stdscr = None

def init(scr):
    """Khởi tạo cấu hình curses"""
    global stdscr
    stdscr = scr
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

def c_print(*args):
    """Thay thế hàm print mặc định"""
    text = " ".join(map(str, args))
    _write_text(text + "\n")
    stdscr.refresh()

def c_input(prompt=""):
    """Thay thế hàm input mặc định"""
    _write_text(str(prompt))
    stdscr.refresh()
    return stdscr.getstr().decode()

def nhap_so_nguyen(prompt):
    """Kiểm tra và ép kiểu nhập số nguyên"""
    while True:
        value = c_input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            c_print("Vui long nhap mot so nguyen.")