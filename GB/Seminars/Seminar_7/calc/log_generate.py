# Модуль записи логов

def write_data(data):
    data = ''.join(map(str, data))
    with open(r'E:\УЧЕБА\Python\GB\Seminars\Seminar_7\calc\log.xml', 'a') as file:
        file.write(data + '=')


def write_result(result):
    result = ''.join(map(str, result))
    with open(r'E:\УЧЕБА\Python\GB\Seminars\Seminar_7\calc\log.xml', 'a') as file:
        file.write(result + '\n')
