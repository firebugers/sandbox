# -*- coding: utf-8-*-
#Создание списка целых, например, [3, 5, 1, 6, 7]
from random import *
#A=[randint(1,22) for x in range(1,6)]
A=[12,16,4,18,3]
print A
# Сортировка списка методом пузырька (без использования языковых конструкций типа sorted)
z=0
while z!=1:
    for x in range(len(A)-1):
        if A[x]>A[x+1]:
            A[x],A[x+1]=A[x+1],A[x]
            break
    else:
        z=1
print A
# Создание из списка словаря вида {3: 0, 5: 1, 1: 2, 6: 3, 7: 4}, где значениями словаря являются индексы ключей списка (HINT: использовать enumerate)
n=list(enumerate(A))
f={}
for x,y in n:
    f[y]=x
print f, len(f)
# Смена у словаря местами ключей и значений. 
f={y:x for x,y in f.items()}   
print f, len(f)  
