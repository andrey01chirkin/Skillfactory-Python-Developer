# С помощью цикла (for или while на выбор) и проверки условий напишите программу,
# которая будет считать произведение всех нечетных чисел от 1 до 10. Полученное
# значение выведите в консоль.

# Инструкция к выполнению задания:
#
# Создайте переменную multipl = 1 для подсчета произведения чисел.
# Составьте цикл с перебором чисел от 1 до 10. Цикл может быть for или while.
# В цикле добавьте проверку условий: если число четное — пропускайте итерацию,
# если нечетное — добавляйте в итоговое произведение.
# После работы цикла выведите полученное произведение
# Критерии оценки:
#
# В программе используется один из видов цикла и проверка условий, правильно
# вычисляется произведение нечетных чисел от 1 до 10.

multipl = 1

for i in range(1, 11):
    if i % 2 != 0:
        multipl *= i

print("Произведение всех нечетных чисел от 1 до 10:", multipl)








