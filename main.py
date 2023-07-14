import random      # ПЕРВОЕ ЗАДАНИЕ
########################################################################################
spisok = [random.randint(-10,50) for _ in range(10)]

num3x = (spisok[3]) * (spisok[6]) * (spisok[9])
numMINMAX = spisok[1:9]                            #---- рабочая переменная, не для вывода!!!
n1, n2, n3, n4, n5, n6, n7, n8 = numMINMAX         #---- рабочая переменная, не для вывода!!!
numminmax = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8  # --- декомпозиция через 2 переменных

negative = 0
for n in spisok:
    if n < 0:
        negative = negative + n

para = 0
nepara = 0
for Zpara in spisok:
    if Zpara % 2 == 0:
        para = Zpara + para

for Znepara in spisok:
    if Znepara % 2 != 0:
        nepara = Znepara + nepara

############################################################################################ ВТОРОЕ ЗАДАНИЕ
spisokPLUS = []
spisokPARA = []
spisokNEPARA = []
spisokMINUS = []

for cc in spisok:
    if cc < 0:
        spisokMINUS.append(cc)

for dd in spisok:
    if dd > 0:
        spisokPLUS.append(dd)

for PaRa in spisok:
    if PaRa % 2 == 0:
        spisokPARA.append(PaRa)

for NePaRa in spisok:
    if NePaRa % 2 != 0:
        spisokNEPARA.append(NePaRa)

##### СНИЗУ БУДЕТ ВЫВОД СРАЗУ ДЛЯ ПЕРВОГО И ВТОРОГО ЗАДАНИЯ
print(f"сумма негативных чисел из (первого)материнского списка: {negative}")
print(f"сумма парных чисел из (первого) материского списка: {para}")
print(f"сумма непарных чисел из (первого) материского списка: {nepara}")
print(f"произвидение чисел кратным 3 из (первого) материнского списка: {num3x}")
print(f"произвидение чисел между минимальным и макс. числом из первого списка: {numminmax}")
print(f"парные числа из первого списка в новом списке: {spisokPARA}")
print(f"непарные числа из первого списка в новом списке: {spisokNEPARA}")
print(f"негативные числа из первого списка в новом списке: {spisokMINUS}")
print(f"позитивные числа из первого списка в новом списке: {spisokPLUS}")
print(f"изначальный первый список ЧИСЕЛ: {spisok}")


