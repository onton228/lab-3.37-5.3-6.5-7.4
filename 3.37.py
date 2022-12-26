# 3.37 Дан список списков, состоящий из t элементов,
# каждый из которых содержит t целых чисел. Найти наибольшие
# элементы среди элементов, имеющих одинаковые порядковые номера.
# Вычислить и напечатать сумму найденных наибольших элементов.
def numderInput(massage):
    while True:
        number = input(massage)

        try:
            number = int(number)
        except ValueError:
            print('Введено не число или не целое число')
        else:
            return number

numbersList = [[2,9,3],[4,8,6],[1,9,5]]

array = zip(*numbersList)
sum = 0

for i in array:
    sum += max(i)

print(f'Сумма всех наибольших элементов по порядковому номеру:{sum}')