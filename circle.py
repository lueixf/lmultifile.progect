# автор работы lueixf


#  функция с вычислениями
def circle(a):
    b = (2*3.14*a)
    c = (3.14*a**2)

    return(b,c)


# функция main
def main():
    a = float(input('введите радиус круга в см '))
    print('длинна окружности равна', circle(a))
    print('площадь окружности равна', circle(a))
    (circle(a))


# вызов функции main
if __name__ == '__main__':
    main()