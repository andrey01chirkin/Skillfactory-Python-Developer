
# Условие: Вам дан список цен на товары в долларах и отношение к курсу евро. С помощью функции map преобразуйте
# данные цены в валюту евро.
# Выводить на экран ничего не надо, лишь создать список и сохранить его в предложенной переменной.

prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

prices_in_euro = list(map(lambda x: x*exchange_rate, prices_in_usd))
print(prices_in_euro)
