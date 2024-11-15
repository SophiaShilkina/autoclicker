import pygetwindow as gw
import psutil
import win32gui
import win32process

from process import is_process_running, process_name


window_title = 'RAGE Multiplayer'

windows = gw.getAllTitles()  # Получаем список всех открытых окон

if window_title in windows:
    print(f'Окно с заголовком "{window_title}" найдено.')
else:
    print(f'Окно с заголовком "{window_title}" не найдено.')
    pid_gta = is_process_running(process_name)

    def get_window_handle_by_pid(pid_gta):
        hwnds = []

        def enum_windows_callback(hwnd, _):
            try:
                _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
                if window_pid == pid_gta:
                    hwnds.append(hwnd)
            except Exception as e:
                pass

        win32gui.EnumWindows(enum_windows_callback, None)
        return hwnds[0] if hwnds else None


    hwnd = get_window_handle_by_pid(pid_gta)
    if hwnd:
        print(f"HWND для процесса {pid_gta}: {hwnd}")
        window_title = win32gui.GetWindowText(hwnd)
        print(f"window_title = {window_title}")
    else:
        print(f"Не найдено окно для процесса {pid_gta}.")


def capture_window(window_title):
    while True:
        try:
            window = gw.getWindowsWithTitle(window_title)[0]
            if window.isMinimized:
                window.restore()
            window.activate()
            window.moveTo(448, 156)
            window.resizeTo(1024, 768)
            break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


def find_the_range():

    if is_process_running(process_name):
        capture_window(window_title)
        print(f"{process_name} запущен1.")
        return True
    else:
        print(f"{process_name} не запущен.")
        return False
