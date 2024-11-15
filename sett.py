import os


base_path = os.path.dirname(os.path.abspath(__file__))
settings_file = os.path.join(base_path, 'settings.txt')


def read_config(settings_file):
    config = {}
    with open(settings_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config


config = read_config(settings_file)
TOKEN = config['TOKEN']
CHAT_ID = config['CHAT_ID']
print(f'{TOKEN, CHAT_ID}')
