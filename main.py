# общий файл с программами
# автор всё так же lueixf


# импорт всех необходимых библиотек и программ
import is_prime as pr # import my own is_prime
import is_even as ev # import my own is_even
import sum as s # import my own sum


#
def main():
    choise = input('если вы хотите вычислить сумму ряда введите 1\n если узнать простое число или нет-2\n если узнать чётность числа - 3\n    ')
    if choise == '1':
        s.main()
    elif choise == '2':
        pr.main()
    elif choise == '3':
        ev.main()




if __name__ == '__main__':
    main()