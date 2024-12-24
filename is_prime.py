# выявление каким является число: простым или нет
# автор работы lueixf


#  функция с вычислениями
def prime (a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    
    return(k)


# функция main
def main():
    a = int(input("Введите число: "))
    k = prime(a)
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")


# вызов функции main
if __name__ == '__main__':
    main()