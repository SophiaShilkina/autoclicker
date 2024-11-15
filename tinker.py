import tkinter as tk
from tkinter import PhotoImage
import keyboard
import time
import threading
import os

from botfarm import start_clicker, stop_clicker
from time_port import stop_time_port
from botafk import start_afk, stop_afk
from wheel_go import start_wheel, stop_wheel
from tgbot import bot
from range import find_the_range

is_on_port = False
is_on_afk = False
is_on_wheel = False
current_time_stop = False
current_time_port = 0
crush_bot = False


def run():
    print('бот запущен')
    run = threading.Thread(target=proc_bot, daemon=True)
    run.start()


def proc_bot():
    threading.Thread(target=bot.polling, daemon=True).start()
    while True:
        time.sleep(1)
        if crush_bot is True:
            bot.stop_polling()
            print('бот остановлен')


class CounterApp:
    def __init__(self, master):
        def switch_port():
            global is_on_port

            if not is_on_port:
                self.button_port.config(image=on)
                start_clicker()
                is_on_port = True
                print(f'порт 1 {is_on_port}')
            else:
                self.button_port.config(image=off)
                stop_clicker()
                stop_time_port()
                is_on_port = False
                print(f'порт 2 {is_on_port}')

        def switch_afk():
            global is_on_afk

            if not is_on_afk:
                self.button_afk.config(image=on)
                start_afk()
                is_on_afk = True
                print(f'афк 1 {is_on_afk}')
            else:
                self.button_afk.config(image=off)
                stop_afk()
                is_on_afk = False
                print(f'афк 2 {is_on_afk}')

        keyboard.add_hotkey('f4', switch_port)

        def switch_wheel():
            global is_on_wheel

            if not is_on_wheel:
                self.button_wheel.config(image=on)
                start_wheel()
                is_on_wheel = True
            else:
                self.button_wheel.config(image=off)
                stop_wheel()
                is_on_wheel = False

        def close():
            global is_on_port, is_on_afk, is_on_wheel, crush_bot

            if is_on_port:
                stop_clicker()
                stop_time_port()
                is_on_port = False
                time.sleep(0.1)

            if is_on_afk:
                stop_afk()
                is_on_afk = False
                time.sleep(0.1)

            if is_on_wheel:
                stop_wheel()
                is_on_wheel = False
                time.sleep(0.1)

            crush_bot = True

            time.sleep(1)

            root.quit()
        self.master = master
        self.master.title("Счетчик")

        # Инициализация счетчика
        self.counter_value = 0
        self.label_port = tk.Label(master, text=f"Порт", fg="white", font=("Helvetica", 10, "bold"), bg="#49423d")
        self.label_port.grid(column=0, row=0, padx=20, pady=10)

        self.button_port = tk.Button(master, image=off, bd=0, command=switch_port, bg="#49423d")
        self.button_port.grid(column=1, row=0, padx=20, pady=10)

        self.label_afk = tk.Label(master, text="Антиафк", fg="white", font=("Helvetica", 10, "bold"), bg="#49423d")
        self.label_afk.grid(column=0, row=1, padx=20, pady=10)

        self.button_afk = tk.Button(master, image=off, bd=0, command=switch_afk, bg="#49423d")
        self.button_afk.grid(column=1, row=1, padx=20, pady=10)

        self.label_wheel = tk.Label(master, text="Колесо", fg="white", font=("Helvetica", 10, "bold"), bg="#49423d")
        self.label_wheel.grid(column=0, row=2, padx=20, pady=10)

        self.button_wheel = tk.Button(master, image=off, bd=0, command=switch_wheel, bg="#49423d")
        self.button_wheel.grid(column=1, row=2, padx=20, pady=10)

        self.exit_button = tk.Button(master, text="Закрыть", bg="red", fg="white", font=("Helvetica", 10, "bold"),
                                command=close)
        self.exit_button.grid(column=0, row=3, padx=20, pady=10)

        self.label_counter = tk.Label(master, text=str(self.counter_value), fg="black", font=("Helvetica", 10))
        self.label_counter.grid(column=0, row=4, columnspan=2,
                                pady=20)  # Счётчик на отдельной строке и с объединением столбцов

        # Кнопка для запуска счетчика
        self.start_button = tk.Button(master, text="Старт", command=self.start_counter)
        self.start_button.grid(column=0, row=5, pady=5)

        # Кнопка для остановки счетчика
        self.stop_button = tk.Button(master, text="Стоп", command=self.stop_counter)
        self.stop_button.grid(column=1, row=5, pady=5)

        # Состояние работы счетчика
        self.running = False

    def update_counter(self):
        if self.running:
            self.counter_value += 1  # Увеличиваем значение счетчика
            self.label_counter.config(text=str(self.counter_value))  # Обновляем текст метки счетчика
            self.master.after(1000, self.update_counter)  # Запланировать следующий вызов через 1 секунду

    def start_counter(self):
        if not self.running:  # Запускаем счетчик только если он не работает
            self.running = True
            self.update_counter()  # Запускаем обновление счетчика

    def stop_counter(self):
        self.running = False  # Останавливаем счетчик


root = tk.Tk()
root.overrideredirect(True)
root.configure(bg="#49423d")
root.geometry("180x320+220+270")
root.wm_attributes('-alpha', 0.85)


base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'data')
os.chdir(data_path)

path_on = 'on.png'
path_off = 'off.png'

on = PhotoImage(file=path_on)
off = PhotoImage(file=path_off)

counter_app = CounterApp(root)


def start_gui():
    if find_the_range():
        root.mainloop()
