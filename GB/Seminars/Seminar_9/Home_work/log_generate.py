# Модуль записи логов

def write_data(data):
    data = ''.join(map(str, data))
    with open('log.xml', 'a', encoding='utf=8') as file:
        file.write(data + '\n')


def read_log():
    with open('log.xml', encoding='utf=8') as log_file:
        print(*log_file.readlines())
