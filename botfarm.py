import pyautogui
import time
import cv2
import numpy as np
from threading import Thread
import os

from range import find_the_range
from time_port import t_port, start_time_thread
from tgbot import send_screenshot, chat_id
from wheel_go import run_wheel


time.sleep(1)
stop_port = True
stop_slash = False
location_close = None


def start_clicker():
    global stop_port
    stop_port = False
    click_thread = Thread(target=checking_the_port)
    click_thread.start()


def stop_clicker():
    global stop_port
    stop_port = True
    print(f'botfarm.py {stop_port}')


def checking_the_port():
    print("botfarm.py функция включена")
    while not t_port and not stop_port:
        print("botfarm.py зашел в цикл")
        find_the_range()
        if find_the_range():
            global stop_slash
            stop_slash = True
            find_the_range()
            pyautogui.press('/')
            print("нажат /")
            time.sleep(2)
            find_the_range()
            pyautogui.press('/')
            print("нажат /")
            stop_slash = False
            # Проверяем, найдено ли окно отмены
            global location_close
            location_close = find_window_close()
            print(location_close)
            if location_close:
                print("Окно отмены найдено, листаю...")
                find_the_range()
                pyautogui.moveTo(location_close)
                pyautogui.scroll(-1000)
                time.sleep(5)

                # Проверяем, найдено ли окно порта
                location_port = find_window_port()
                if location_port:
                    find_the_range()
                    pyautogui.click(location_port)
                    print("Окно порта найдено, кликаю...")
                    time.sleep(5)

                    # Проверяем, найдено ли окно заказа
                    location_order = find_window_order()
                    if location_order:
                        find_the_range()
                        pyautogui.click(location_order)
                        print("Окно заказа найдено, кликаю...")
                        send_screenshot(chat_id)
                        time.sleep(5)
                        run_wheel()
                        location_close = None
                        start_time_thread()
                    else:
                        time.sleep(3)
            else:
                time.sleep(15)
        else:
            time.sleep(15)


def find_window_port():
    # Выравниваем окно
    find_the_range()
    time.sleep(1)
    # Делаем снимок экрана
    screenshot = pyautogui.screenshot(region=(448, 156, 1024, 768))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Загружаем изображение шаблона
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, 'data')
    os.chdir(data_path)
    name = 'port.bmp'

    port_img = cv2.imread(name)
    print(f'order_img {port_img}')
    h, w, _ = port_img.shape

    # Ищем совпадений
    result = cv2.matchTemplate(screenshot, port_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    yloc, xloc = np.where(result >= threshold)
    yloc += 156
    xloc += 448

    if len(xloc) > 0 and len(yloc) > 0:
        # Возвращаем координаты центра найденного окна
        return xloc[0] + w // 2, yloc[0] + h // 2
    return None


def find_window_order():
    find_the_range()
    time.sleep(1)

    screenshot = pyautogui.screenshot(region=(448, 156, 1024, 768))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, 'data')
    os.chdir(data_path)
    name = 'vzat_zakaz.bmp'

    order_img = cv2.imread(name)
    print(f'order_img {order_img}')
    h, w, _ = order_img.shape

    result = cv2.matchTemplate(screenshot, order_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    yloc, xloc = np.where(result >= threshold)
    yloc += 156
    xloc += 448

    if len(xloc) > 0 and len(yloc) > 0:
        return xloc[0] + w // 2, yloc[0] + h // 2
    return None


def find_window_close():
    find_the_range()
    time.sleep(1)

    screenshot = pyautogui.screenshot(region=(448, 156, 1024, 768))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, 'data')
    os.chdir(data_path)
    name = 'otmena.bmp'

    close_img = cv2.imread(name)
    print(f'close_img {close_img}')
    h, w, _ = close_img.shape

    result = cv2.matchTemplate(screenshot, close_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    yloc, xloc = np.where(result >= threshold)
    yloc += 96
    xloc += 448

    if len(xloc) > 0 and len(yloc) > 0:
        return xloc[0] + w // 2, yloc[0] + h // 2
    return None
