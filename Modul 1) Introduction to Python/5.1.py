#------------------------------------------------------------------------------------------------------------------------------------
# 5.1
# Напишите программу, которая берёт из строки срез символов с 8-й по 42-ю позицию включительно
# и выводит на печать каждый третий символ. Перед взятием среза проверьте, что строка достаточной
# длины. Если недостаточной, программа должна напечатать сообщение об ошибке. Например, для строки
# длиной 20 символов оно должно быть таким: «length error: длина строки составляет 20 символов». Что
# будет, если эту проверку не реализовать, а строка окажется недостаточно длинной (то есть верхняя
# граница среза выйдет за границу строки)?
#
# Пример: из строки 'abcdefghijk 1456 ahalai-mahalai! Восстань, сын трёхголового дракона!' должен
# получиться такой результат: 'hk4 aial!оть'.

str = "abcdefghijk 1456 ahalai-mahalai! Восстань, сын трёхголового дракона!"

if len(str) > 42:
    print("5.1: ", str[7:42:3])
else:
    print("5.1: ", "length error: длина строки составляет", len(str), "символов")