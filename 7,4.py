# 7.4 Опишите, используя словарь, школьную нагрузку
# (фамилия преподавателя, класс, часы). Составьте программу,
# определяющую нагрузку каждого преподавателя. Определить,
# у какого преподавателя самая большая нагрузка и у кого самая низкая.

# Функция проверки ввода строки на пустоту
def textInput(massage):
    while True:
        text = input(massage)

        if len(text.strip()) ==0:
            print('Введите Текст')
        else:
            return text

# Функция проверки ввода чисел
def numberInput(massage):
    while True:
        number = input(massage)

        try:
            number = int(number)
        except ValueError:
            print('Введено не число или не целое число')
        else:
            return number

# Ввод данных
schoolLoad = {}

while True:
    teacher = textInput('Введите имя преподавателя')
    if (teacher.lower() == 'stop') or (teacher.lower() == 'стоп'):
        break
    group = numberInput('Введите класс:')
    hours = numberInput('Введите школьную нагрузку:')
    print('')

    # Проверка на существование ключа
    if teacher in schoolLoad:
        schoolLoad[teacher] = schoolLoad[teacher] + [(group,hours)]
    else:
        schoolLoad[teacher] = [(group,hours)]
# Имя: [ (Класс, часы)]
# schoolLoad = {'Воронцов':[(11,2),(10,2),(9,2)],
#               'Нестеров':[(7,3),(9,2),(6,1)],
#               'Портнягин':[(6,5),(7,1),(11,3)]}

maxHourTeacher = ''
minHourTeacher = ''
maxHour = 0
minHour = 1000000

for teacher,information in schoolLoad.items():
    sumHour = 0
    for group, hour in information:
        sumHour += hour
    if maxHour < sumHour:
        maxHour = sumHour
        maxHourTeacher = teacher
    if minHour > sumHour:
        minHour = sumHour
        minHourTeacher = teacher

if len(schoolLoad) > 1:
    print(f'Самая большая нагрузка у преподавателя {maxHourTeacher}: {maxHour}\nМинимальная нагрузка у преподавателя {minHourTeacher}: {minHour}')
elif len(schoolLoad) == 1:
    print(f'Нагрузка у преподавателя {maxHourTeacher}: {maxHour}')
else:
    print('Список нагрузки преподавателей пуст')


