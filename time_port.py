import time
from threading import Thread


t_port = 0
running = True


def time_port(callback):
    print('time_port.py зашел в функцию')
    global t_port
    t_port = 420
    while running and t_port:
        time.sleep(1)
        t_port -= 1
        print(t_port)
        callback(t_port)


def start_time_thread():
    global running
    running = True
    time_port_thread = Thread(target=time_port, args=(callback,))
    time_port_thread.start()
    time_port_thread.join()


def stop_time_port():
    global running
    running = False
