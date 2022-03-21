"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]

Input: candidates = [2], target = 1
Output: []
"""

import json

candidates = json.loads(input())
target = int(input())

result = []

def recursion(tl = []):
    if sum(tl) == target:
        result.append(tl.copy())
        return

    for i in candidates:
        if (sum(tl) + i) <=  target:
            tl.append(i)
            recursion(tl.copy())
            tl.pop()

recursion()

print([list(j) for j in list(set([tuple(sorted(i)) for i in result]))])