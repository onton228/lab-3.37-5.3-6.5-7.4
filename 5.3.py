# 5.3 Дано натуральное число n. Среди чисел 1, 2, ... , n
# найти все те, которые можно представить в виде
# суммы квадратов двух натуральных чисел, определив функцию,
# позволяющую распознавать полные квадраты.
def isFullSquare(n):
    return n**(1/2) == round(n**(1/2))

# Проверка ввода чисел

while True:
    n = input('Введите натуральное число: ')

    try:
        n=int(n)
    except ValueError:
        print('Введено не число')
    else:
        if n <= 0:
            print('Введено не натуральное число')
        else:
            break

multiplicity = set()

for i in range(1,n+1):
    if isFullSquare(i):
        for j in range(1, n+1):
            if isFullSquare(j) and (i + j <= n):
                multiplicity.add(i+j)

if len(multiplicity) !=0:
    print(f'Числа которые можно представить в виде суммы квадратов:{";".join([str(x) for x in sorted(multiplicity)])}')
else:
    print('Среди данной последовательности нет чисел, которые можно представить в виде суммы квадратов')