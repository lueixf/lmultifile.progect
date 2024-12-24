# автор работы lueixf


#  функция с вычислениями
def even(a):
    return(a)



# функция main
def main():
    a = float(input('введите число '))
    if (a % 2 == 0):
        print('число', a , 'чётное')
    else:
        print('число', a , 'нечётное')
    (even(a))


# вызов функции main
if __name__ == '__main__':
    main()