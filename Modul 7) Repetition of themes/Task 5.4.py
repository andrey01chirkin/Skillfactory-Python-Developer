
#Из списка в предыдущем задании найти кортеж с минимальным индексом массы тела

# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

print(min(data, key=lambda x: x[0]/x[1]**2))


