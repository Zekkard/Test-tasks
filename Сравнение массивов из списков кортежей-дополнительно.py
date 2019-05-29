# ������ ������ ������ ��� ������ �� ������ �������� �� ���������� �����������. 
# � ������ ����������� �������� ��� ������� � �������� ����������� ��������� ��������.
# �������� ����� ������, �������������� ������ ������� �� ��������.


# ������.
import numpy as np
from itertools import groupby
from operator import itemgetter, sub

# ������, � ������� �������� ������ �� ��������. ������ ����� �� �������.
var1 = np.array([(6,8), (10,15), (19,23)]) 
var2 = np.array([(7,12), (19,22)])
Lst1 = []
Lst2 = []
Answer_pool = []
Answer = []

# ���������� �������� � ���������� ������������������� ��� ������� ���������� ������� � ��������������� ���������� � ���������.
for (w, x) in var1:
    Lst1.append(np.arange(w,x+1))
tup1 = np.concatenate(Lst1, axis=0)
tup_con1 = set(tuple(tup1))
for (y, z) in var2:
    Lst2.append(np.arange(y,z+1))
tup2 = np.concatenate(Lst2, axis=0)
tup_con2 = set(tuple(tup2))

# ��������� ��������.
Digits_ranges = (tup_con1 & tup_con2)

# ����������� �������-�������� ������������������ �� ������, �������� �� ������ ��������.
for q in Digits_ranges:
    Answer_pool.append(int(q))
for d, e in groupby(enumerate(Answer_pool), lambda x: sub(*x)):
    items = list(map(itemgetter(1), e))
    if len(items) > 1:
        Answer.append( (items[0],items[-1]) )
    else:
        Answer.append((items[0]))
print(Answer)