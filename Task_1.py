# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

number_A = int(input("Введлите число A: "))
number_B = int(input("Введите степень B: "))
def A_Power_B (number_A, number_B):
    if (number_B == 1):
        return(number_A)
    if (number_B != 1):
        return (number_A * A_Power_B(number_A, number_B - 1))
print("Число А, возведенное в степень В равно:", A_Power_B(number_A, number_B))