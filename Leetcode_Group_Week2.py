# DATE: March 8th, 2024
# Week 2

"""
724. Find Pivot Index (ARRAYS)(EASY)
392. Is Subsequence (ARRAYS)(EASY)
121. Best Time to Buy and Sell Stock I (GREEDY)(EASY)
122. Best Time to Buy and Sell Stock II (FOR LOOP)(MEDIUM)
"""


# ---------------------------------------------------------------------------------

# 724. Find Pivot Index (ARRAYS)(EASY)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

# LIST OF INT GIVEN. FIND THE INDEX WHERE SUM OF LEFT AND RIGHT ARE EQUAL

# 1. Loop through the array.
# 2. Add up numbers and multiply by 2. That number + current number must equal total.

        total = sum(nums)  # sum method is O(N)
        cur_sum = 0
        
        for i in range(len(nums)):  # for loop is O(N)

            if (cur_sum * 2) + nums[i] == total:
                return i
            
            cur_sum += nums[i]
        
        # If no answer found, return -1
        return - 1

# Time: O(N): O(2N) -> O(N)
# Space: O(1): Uses constant extra memory.


# ---------------------------------------------------------------------------------


# 392. Is Subsequence (ARRAYS)(EASY)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
# TWO STR S AND T GIVEN. FIND OUT IF S IS IN T IN THE GIVEN ORDER

# 1. We will be using two pointer. i and j pointers both start at 0. 
# 2. Increment j on t array at every loop.
# 3. If letter where j is pointing at t is found at where i is pointing at s, increment i.
# 4. Return a boolean if all the letters of s can be found on t in order.

        i, j = 0, 0

        # Increment j while you ONLY increment i when the letter at i and j matches.
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        # i will equal len(s) if all letters in s was seen in t.
        return i == len(s)
        

# Time: O(N): Loops once
# Space: O(1): Uses constant extra memory


# ---------------------------------------------------------------------------------


# 121. Best Time to Buy and Sell Stock I (GREEDY)(EASY)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

# We will be using the method Greedy.

# 1. Assign min_buy to inf so that first value will update it. 
# 2. Assign max_profit to 0 so we can keep track.
# 3. Iterate through the array once:
    # a. Keep track of min buy price. Update max_profit between diff and max_profit

        ## Edge Case.
        if not prices:
            return 0
        
        ## Assign min_buy and max_profit.
        min_buy = float('inf')
        max_profit = 0

        ## At every loop: Update min_buy and max_profit.
        for price in prices:
            min_buy = min(min_buy, price)                 
            max_profit = max(max_profit, price - min_buy)

        return max_profit

# Time: O(N): Iterates through the array once using loop
# Space: O(1): Only uses fixed amount of extra space.


# ---------------------------------------------------------------------------------


# 122. Best Time to Buy and Sell Stock II (FOR LOOP)(MEDIUM)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
# 1. Assign total_profit to 0 so we can keep track.
# 2. Iterate through the array once. 
    # a. If current price is greater than previous price. Add diff to total_profit.
        
        ## Edge Case.
        if not prices:
            return 0
        
        ## Assign total_profit
        total_profit = 0

        ## At every loop: if cur is greater than prev, add diff to total_profit.
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit

# Time: O(N): Iterates through the array once using loop
# Space: O(1): Only uses fixed amount of extra space.