'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''

import json

candidates = json.loads(input())
target = int(input())

class Solution:
    def combination_sum2(self, candidates, target):
        result = []
        if sum(candidates) < target:
            return []
        if len(set(candidates)) == 1:
            mul = target//candidates[0]
            if sum(candidates[:mul]) == target:
                return [candidates[:mul]]
        def recursion(ind = 0 , tl = []):
            if sum(tl) == target:
                if tl not in result:
                    result.append(tl.copy())
                return
            if ind>=len(candidates):
                return

            for i in range(ind, len(candidates)):
                if (sum(tl) + candidates[i]) <=  target:
                    tl.append(candidates[i])
                    recursion(i+1, tl.copy())
                    tl.pop()

        recursion()

        return [list(j) for j in list(set([tuple(sorted(i)) for i in result]))]