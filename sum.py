# нахождение суммы ряда
# автор работы lueixf


# функция с вычислениями
def add (num_list):
     res = float(num_list[0])
     for i in range (1,len(num_list)):
        res += float(num_list[i])
    
     return(res)  

# функция main
def main():
   a = input('введите числа ')
   num_list = a.split()
   b = add(num_list)
   print( 'сумма всех чисел в списке равна ', b)


# вызов функции main
if __name__ == '__main__':
   main() 