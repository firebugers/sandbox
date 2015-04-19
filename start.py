# -*- coding: utf-8-*-
#Создание списка целых, например, [3, 5, 1, 6, 7]
from random import *
#A=[randint(1,22) for x in range(1,6)]
A=[12,16,4,18,3]
print A
# Сортировка списка методом пузырька (без использования языковых конструкций типа sorted)
def list_sorted(l):
    """
    >>> list_sorted([2,5,3,1])
    [1, 2, 3, 5]
    >>> 
    """
    z=0
    while z!=1:
        for x in range(len(l)-1):
            if l[x]>l[x+1]:
                l[x],l[x+1]=l[x+1],l[x]
                break
        else:
            z=1
    print l
list_sorted(A)
# Создание из списка словаря вида {3: 0, 5: 1, 1: 2, 6: 3, 7: 4}, где значениями словаря являются индексы ключей списка (HINT: использовать enumerate)

def list_to_dict(l):
    """
    >>> list_to_dict([1,2,3])
    {1: 0, 2: 1, 3: 2}
    >>>
    """
    f={}
    n=list(enumerate(l))
    for x,y in n:
        f[y]=x
    return f
f=list_to_dict(A)
print f
    # Смена у словаря местами ключей и значений. 
def change_dict(d): 
    """
    >>> change_dict({1:'one',2:'two',3:'three'})
    {'three': 3, 'two': 2, 'one': 1}
    >>>
    """
    if type(d)==dict:   
        d={y:x for x,y in d.items()}   
        print d
    else:
        print 'Give me a dictionary'
        print d, type(d)
change_dict(f)    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
