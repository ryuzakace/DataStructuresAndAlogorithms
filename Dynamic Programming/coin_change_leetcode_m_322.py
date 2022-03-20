'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
'''

import json

coins = json.loads(input())
amount = int(input())

min_c = {}
min_c[0] = 0

for i in range(1,amount+1):
    temp_m = 1e9
    for j in coins:
        if i-j in min_c:
            temp_m = min(temp_m, min_c[i-j]+1)
    min_c[i] = temp_m

if min_c[amount] < 1e9:
    print(min_c[amount])
else:
    print(-1)
