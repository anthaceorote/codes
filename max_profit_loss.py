import random


def max_loss_made(arr):
    buy_date, sell_date = 0, 0
    max_loss = 0
    max_price = arr[0]
    max_date = 0

    for d, p in enumerate(arr):
        if p > max_price:
            max_price = p
            max_date = d + 1
            continue

        loss = max_price - p

        if loss > max_loss:
            max_loss = loss
            buy_date, sell_date = max_date, d + 1

    return (buy_date, sell_date), max_loss


def max_profit_made(arr):
    buy_date, sell_date = 0, 0
    max_profit = 0
    min_price = arr[0]
    min_date = 0

    for d, p in enumerate(arr):
        if p < min_price:
            min_price = p
            min_date = d + 1
            continue

        profit = p - min_price

        if profit > max_profit:
            max_profit = profit
            buy_date, sell_date = min_date, d + 1

    return (buy_date, sell_date), max_profit

random_inp = [random.randrange(50) for _ in range(10)]
print(random_inp)
print(max_loss_made(random_inp))
print(max_profit_made(random_inp))
