# Вторая версия задачи про массив из списка кортежей со временными интервалами. 
# В задаче требовалось сравнить два массива и получить пересечение временных отрезков.
# Уточнили форму вывода, осуществляться должен списком из кортежей.


# Модули.
import numpy as np
from itertools import groupby
from operator import itemgetter, sub

# Переменные.
# Массивы, в которых хранятся список из кортежей. Прямая копия из задания.
var1 = np.array([(6,8), (10,15), (19,23)]) 
var2 = np.array([(7,12), (19,22)])
Lst1 = []
Lst2 = []
Answer_pool = []
Answer = []

# Считывание массивов и вычисление последовательностей для каждого отдельного кортежа с преобразованием результата в множества.
for (w, x) in var1:
    Lst1.append(np.arange(w,x+1))
tup1 = np.concatenate(Lst1, axis=0)
tup_con1 = set(tuple(tup1))
for (y, z) in var2:
    Lst2.append(np.arange(y,z+1))
tup2 = np.concatenate(Lst2, axis=0)
tup_con2 = set(tuple(tup2))

# Сравнение множеств.
Digits_ranges = (tup_con1 & tup_con2)

# Определение минимум-максимум последовательности из списка, создание из вводных данных списка кортежей.
for q in Digits_ranges:
    Answer_pool.append(int(q))
for d, e in groupby(enumerate(Answer_pool), lambda x: sub(*x)):
    items = list(map(itemgetter(1), e))
    if len(items) > 1:
        Answer.append( (items[0],items[-1]) )
    else:
        Answer.append((items[0]))
print(Answer)
