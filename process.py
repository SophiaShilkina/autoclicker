import psutil


process_name = 'loginom.exe'


def is_process_running(process_name):
    # Перебираем все запущенные процессы
    for proc in psutil.process_iter(['name']):
        try:
            if proc.name() == process_name:
                return proc.pid
        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    return False


if is_process_running(process_name):
    print(f"{process_name} запущен.")
else:
    print(f"{process_name} не запущен.")
