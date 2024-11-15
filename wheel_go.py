import pyautogui
import time
import cv2
import numpy as np
import threading
import os

from range import find_the_range
from tgbot import send_screenshot, CHAT_ID


stop_wheel_p = True
location_wheel = None


def start_wheel():
    global stop_wheel_p
    stop_wheel_p = False
    print(stop_wheel_p)


def stop_wheel():
    global stop_wheel_p
    stop_wheel_p = True


def run_wheel():
    click_thread = threading.Thread(target=checking_the_wheel)
    click_thread.start()


def checking_the_wheel():
    print("wheel.py функция включена")
    while True:
        print("wheel.py зашел в цикл")
        global location_wheel
        location_wheel = find_window_wheel()
        if location_wheel is not None and not stop_wheel_p:
            print("wheel.py начал выполнение")
            find_the_range()
            pyautogui.press('up')
            time.sleep(15)
            find_the_range()
            pyautogui.click(1391, 884)  # Сафари
            time.sleep(15)
            find_the_range()
            pyautogui.click(972, 860)  # Даймонд
            time.sleep(15)
            find_the_range()
            pyautogui.click(638, 496)  # Колесо удачи
            time.sleep(15)
            find_the_range()
            pyautogui.click(963, 800)   # Крутить колесо
            time.sleep(25)
            send_screenshot(CHAT_ID)
            find_the_range()
            pyautogui.press('esc')
            location_wheel = None
        else:
            break


def find_window_wheel():
    find_the_range()
    time.sleep(1)

    screenshot = pyautogui.screenshot(region=(448, 156, 1024, 768))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, 'data')
    os.chdir(data_path)
    name = 'koleso.bmp'

    wheel_img = cv2.imread(name)
    print(f'wheel_img {wheel_img}')
    h, w, _ = wheel_img.shape

    result = cv2.matchTemplate(screenshot, wheel_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    yloc, xloc = np.where(result >= threshold)
    yloc += 156
    xloc += 448

    if len(xloc) > 0 and len(yloc) > 0:
        return xloc[0] + w // 2, yloc[0] + h // 2
    return None
