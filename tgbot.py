import telebot
import pyautogui
import threading

from range import find_the_range
from sett import CHAT_ID, TOKEN


bot = telebot.TeleBot(TOKEN)
chat_id = CHAT_ID


def send_screenshot(chat_id):
    find_the_range()
    # Делаем скриншот
    screenshot = pyautogui.screenshot(region=(448, 156, 1024, 768))

    # Сохраняем скриншот во временный файл
    screenshot.save('screenshot.png')

    # Отправляем скриншот как фото
    with open('screenshot.png', 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


@bot.message_handler(commands=['new'])
def handle_new_command(message):
    print('соо отправлено')
    global thread
    thread = threading.Thread(target=send_screenshot, args=(message.chat.id,))
    thread.start()
