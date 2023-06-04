# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 
number_A = int(input("Введите число А: "))
number_B = int(input("Введите число В: "))
def recursive_sum (number_A, number_B):
    if number_B == 0:
        return number_A
    return 1 + recursive_sum(number_A, number_B - 1)
print("Сумма:",recursive_sum(number_A, number_B))