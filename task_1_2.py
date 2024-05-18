import timeit
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum, coins):
    actual_sum = sum
    calculation = {}
    for coin in coins:
        n = 0
        while actual_sum >= coin:
            actual_sum -= coin
            n += 1    
        if n > 0: calculation[coin] = n
    return calculation





def find_min_coins(sum, coins):
    dp = [float('inf')] * (sum + 1)
    
    dp[0] = 0
    coin_used = [[] for _ in range(sum + 1)]
    
    for i in range(1, sum + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]
    
    result = {}
    for coin in coin_used[sum]:
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
    
    return result


sum = 113

print("Greedy alorythm result:")
print(find_coins_greedy(sum,coins))
print("Dynamic alorythm result:")
print(find_min_coins(sum,coins))

test1 = timeit.timeit('find_coins_greedy(100,coins)', globals=globals(), number=1000)
test2 = timeit.timeit('find_min_coins(100,coins)', globals=globals(), number=1000)
print("Test1:",test1)
print("Test2:",test2)
test3 = timeit.timeit('find_coins_greedy(10000,coins)', globals=globals(), number=1000)
test4 = timeit.timeit('find_min_coins(10000,coins)', globals=globals(), number=1000)
print("Test3:",test3)
print("Test4:",test4)
coins2 = [49, 23, 8, 4, 2, 1]
test5 = timeit.timeit('find_coins_greedy(10000,coins2)', globals=globals(), number=1000)
test6 = timeit.timeit('find_min_coins(10000,coins2)', globals=globals(), number=1000)
print("Test5:",test5)
print("Test6:",test6)
