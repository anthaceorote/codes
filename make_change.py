def make_change(change_reqd, coin_list, min_coins, coin_traceback):
    for cents in range(change_reqd + 1):
        coin_count = cents
        new_coin = sorted(coin_list)[0]
        for c in [coin for coin in coin_list if coin <= cents]:
            if min_coins[cents - c] + 1 < coin_count:
                coin_count = min_coins[cents - c] + 1
                new_coin = c
        min_coins[cents] = coin_count
        coin_traceback[cents] = new_coin
    return min_coins[change_reqd]


def num_ways_to_make_change(coin_list, change_reqd):
    change_made = [0] * (change_reqd + 1)
    change_made[0] = 1

    for coin in coin_list:
        for j in range(coin, change_reqd + 1):
            change_made[j] += change_made[j - coin]

    return change_made[change_reqd]


def print_coins_reqd(coin_traceback, change_reqd):
    coin = change_reqd
    coins_used = []
    while coin > 0:
        coin_used = coin_traceback[coin]
        coins_used.append(coin_used)
        coin = coin - coin_used
    return coins_used


def compute_change(change_reqd, coin_list, debug=False):
    min_coins = [0] * (change_reqd + 1)
    coin_traceback = [0] * (change_reqd + 1)

    min_coins_reqd = make_change(change_reqd, coin_list, min_coins, coin_traceback)

    if debug:
        print("Making change for %d amount requires a minimum of %d coins" % (change_reqd, min_coins_reqd))
        print("Min coins required =", print_coins_reqd(coin_traceback, change_reqd))

    return min_coins, coin_traceback


def main():
    change_reqd = 63
    coin_list = [1, 5, 10, 25]

    _ = compute_change(change_reqd, coin_list, debug=True)

    assert num_ways_to_make_change([1, 2, 3], 4) == 4

if __name__ == '__main__':
    main()
