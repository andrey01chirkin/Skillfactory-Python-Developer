#Напишите числа в порядке возрастания через пробел, которые выведет программа из предыдущего задания,
# если на вход подаются две последовательности чисел:
#1 2 3 4 5 6 7 8
#2 4 6 8 10 12

a_set = {1,2,3,4,5,6,7,8}
b_set = {2,4,6,8,10,12}

print(sorted(a_set.symmetric_difference(b_set)))
