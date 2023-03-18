"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
"""

import random

n = int(input('Введите количество элементов в массиве: '))
A = []
for i in range(n):
    A.append(random.randint(0, 9))
print(*A)
X = int(input('Введите число Х: '))

min_diff = abs(X - A[0])
for i in range(1, n):
    diff = abs(X - A[i])
    if diff < min_diff:
        min_diff = diff
        closest_elem = A[i]

print("Самый близкий элемент к числу", X, "в массиве A:", closest_elem)
