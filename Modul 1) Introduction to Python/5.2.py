#------------------------------------------------------------------------------------------------------------------------------------
#5.2
# Напишите программу, которая проверяет, являются ли все символы строки символами,
# входящими в набор символов ASCII. Если да, программа должна напечатать True, если
# нет — False. Если строка нулевой длины, тоже напечатать False.

str = "Hello"

if len(str) == 0:
    print("5.2: ", "False")
else:
    print("5.2: ", str.isascii())