#Программа должна выводить «Обе переменные ложные», если они являются таковыми.
# Дополните условный оператор последним блоком.

a = 0
b = 'Hello'

if not a and not b:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print( a or b ) # печать одной переменной, которая является истинной
else:
    print("Обе переменные ложные")