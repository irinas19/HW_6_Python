#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from data_module import check_data_view
from sys import argv


if __name__ == '__main__':
    test = input('Введите год в виде DD.MM.YYYY ==> ')
    check_data_view(argv[1])