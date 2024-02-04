from timeit import timeit


def find_coins_greedy(coins, price):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        cnt = price // coin
        if cnt > 0:
            result[coin] = cnt
            price -= coin * cnt

    return result


def find_min_coins(coins, price):
    coins.sort(reverse=True)

    min_coins = [float('inf')] * (price + 1)
    last_used = [0] * (price + 1)

    min_coins[0] = 0
    for i in range(1, price + 1):
        for coin in coins:
            if i - coin >= 0 and min_coins[i] > min_coins[i - coin] + 1:
                min_coins[i] = min_coins[i - coin] + 1
                last_used[i] = coin

    result = {}
    while price > 0:
        result[last_used[price]] = result.get(last_used[price], 0) + 1
        price -= last_used[price]

    return result


def get_time(func, coins, price):
    return timeit(lambda: func(coins, price), number=1000)


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    price = 113

    print(f"Price: {price}")
    print(f"Greedy: {find_coins_greedy(coins, price)}")
    print(f"Dynamic: {find_min_coins(coins, price)}")

    print(f"{'Price':<10} | {'Function':<20} | {'Time':<10}")
    print(f"{'-' * 10:<10} | {'-' * 20:<20} | {'-' * 10:<10}")

    for price in [113, 12345]:
        for func in (find_coins_greedy, find_min_coins):
            print(f"{price:<10} | {func.__name__:<20} | {get_time(func, coins, price):<10}")

