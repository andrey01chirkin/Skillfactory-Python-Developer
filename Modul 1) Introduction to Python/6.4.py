import sys

#------------------------------------------------------------------------------------------------------------------------------------
# 6.4
# Напишите программу, которая делает следующее:
# 1) Запрашивает у пользователя строку с приглашением.
# 2) Выводит это приглашение на печать и в той же строке ожидает ещё одного ввода текста.
# 3) Выводит на печать введённый пользователем в предыдущем пункте текст 3 раза подряд в одну строку. Выводы должны быть разделены знаком “#”.
# 4) * Вывод приглашения в пункте b реализуйте двумя разными способами: с помощью возможностей print() и input().


str = input("Введите строку с пришлашением: ")
print(str)
text = input()
print((text + "#") * 3)

print("Введите строку с пришлашением: ", end="")
line = sys.stdin.readline()
sys.stdout.write(line.strip() + "\n")
text2 = sys.stdin.readline()
sys.stdout.write(((text + "#") * 3) + "\n")