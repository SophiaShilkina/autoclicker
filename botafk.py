import pyautogui
import random
import time
from threading import Thread

from range import find_the_range


stop_afk_p = True


def start_afk():
    global stop_afk_p
    stop_afk_p = False
    click_thread = Thread(target=antiafk)
    click_thread.start()


def stop_afk():
    global stop_afk_p
    stop_afk_p = True
    print(f'botfarm.py {stop_afk_p}')


def antiafk():
    time.sleep(0.2)
    print("botafk.py функция включена")
    while not stop_afk_p:
        print("botafk.py зашел в цикл 1")
        from botfarm import location_close, stop_slash
        from wheel_go import location_wheel
        if location_close is not None or location_wheel is not None or stop_slash:
            time.sleep(3)
        else:
            while location_close is None and location_wheel is None and not stop_afk_p:
                print("botafk.py зашел в цикл 2")
                match random.randint(1, 2):
                    case 1:
                        find_the_range()
                        pyautogui.press('a')
                        print("Нажат символ 'a'")
                        time.sleep(9)
                        from botfarm import location_close
                        from wheel_go import location_wheel
                    case 2:
                        find_the_range()
                        pyautogui.press('d')
                        print("Нажат символ 'd'")
                        time.sleep(9)
                        from botfarm import location_close
                        from wheel_go import location_wheel
