
# DATE: March 1st, 2024

"""
Hey guys, welcome to our first leetcode meeting.

Our goal is to train our brain and learn how to get to the solution no matter
how hard the quesiton is instead of memorizing solutions.

Leetcode is hard and can be overwhelming. That's why we need a good strategy.
So from the beginning, we need practice properly.

It doesn't matter how many problems you have solved before, if you are using
the wrong strategy, it's not going to help you much.


Think of technical interviews as collaborative problem-solving. You are there
to solve that problem with another person. The interviewer doesn't want to see
you just solving a question by yourself.

Two main things interviewers look for:
1. How you handle stress.
2. How you communicate.
3. how you handle feedback. EX: "Yo
    EX: They may not give you all the information to solve the problem,
        They want you to ask questions and communicate with them.
    EX: They may say that you're code is slow and is running O(N^2) time comp.
        They will ask you to optimize your code, and even if you don't know
        a way to optimize, at least know where and why your code is slow.

---------------------------------------------------------------------------------

Topics we will work on:
First we will work on strong data structure foundations.

DATA STRUCTURES
    Arrays
    Hash Tables
    Stacks
    Queues
    Linked Lists
    Trees
    Graphs
    Tries (In a tree, each node holds a value. In a trie, nodes themselves dont hold a value—instead, the value is the path from the root to that node.)

Then we will target each algorithms.
ALGORITHMS
    Binary Search: Use on a sorted list to find elements fast.
    Two Pointers: When solving in place with no extra space.
    Sliding Window: For analyzing subsets within a set.
    BFS/DFS: BFS for shortest path in unweighted graphs; DFS for deep graph exploration.
    Recursion / Backtracking: Recursion for incremental solutions; Backtracking for exploring all possibilities.
    Divide and Conquer: Break problems into smaller, similar problems.
    Dynamic Programming: For overlapping subproblems, saves time with memoization.
    Bit Manipulation: For low-level integer operations.
    Topological Sort: Ordering of vertices in a directed graph without cycles.
    
---------------------------------------------------------------------------------

KEY POINTS for every technical interview.

1. Ask questions and don't assume. Even if you solved the question before,
ask questions as if its your first time. We may not have the luxury of leetcode
telling us all the details regarding the problem.

    EX: You are given a list. Order the numbers inside from least to greatest.

    Are there any constraints to the parameter or solution?
    Will you be dealing with negative numbers?
    Will the numbers be in string or integer form?
    Should I consider edge cases such as empty list?
    Clarify what input they will give and what output they expect.
    Is it okay to use built-in functions?
    what to output if no solution is found?

2. If you are stuck during the coding stage, drop everything and go back to your
pseudocode. If your logic is good, coding part should be easy.

---------------------------------------------------------------------------------

PREP Methodology.

Parameters -- ALWAYS validate input first. Always consider edge case.

Return values -- What the function should return. 
    What output do you need in order for the test to work?

Examples -- Begin working through examples.
    Use examples to clarify edge cases and ensure your solution covers
    all possible scenarios.

Psuedocode -- A way to describe how to solve a problem using a simplified
    form of coding syntax.

psuedocode example:
    prompt: You are given a list. Order the numbers inside from least to greatest.
        1. For each index i in the list:
            a. Find the smallest number in the list from index i to the end
            b. Swap the smallest number found with the number at index i
        2. Return the sorted list


AFTER completion. Discuss how you can optimize. It is normal to sacrifice
space complexity for time complexity.

---------------------------------------------------------------------------------

Additional information links:

BIG O Notation + time complexity table.
https://www.bigocheatsheet.com/

ASCII Table
https://www.asciitable.com/
"""

# ---------------------------------------------------------------------------------

# DATE: March 1, 2024
# Week 1

"""
1. Two Sum (Easy)
242. Valid Anagram (Easy)
49. Group Anagrams (Medium)
125. Valid Palindrome (Easy)
387. First Unique Character in a String (Easy)
"""

# ---------------------------------------------------------------------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

## METHOD: Using one pass hashmap prevents me from using the same number again since that number won't be in the hashmap yet. 
# Time: O(N)
# Space: O(N)

        # dictionary: {difference:index of a, difference:index of a}
        # {7:0, 2:1, -3: 2, ...  }
        # [2, 7, 11, 15]

        # Pseudo code:
        
        
        # 1. Create hashmap to store number and its index

        # 2. For each number in nums:
                # a. Calculate difference between target and current number (difference = target - nums[a])
                
        # 3. If difference is in hashmap: (if I see the difference in the dictionary. that means I found the target.)
                # b. Return [current index, index of difference from hashmap]

        # 4. Store current number and its index in hashmap

        d = {}

        for a in range(len(nums)): 
            diff = target - nums[a] # first loop: 7 = 9 - 2
            
            # check if its in dictionary
            if diff in d:
                return [d[diff], a]
            
            # if not in dictionary, add to dictionary
            d[nums[a]] = a

# Time: O(N)
# Space: O(N)

# ---------------------------------------------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# PREP:

# PARAMETER:
    # two strings in variable. s and t.
        # s = "anagra@#m!"   t = "    naga r  am "
    # lower case only. 
    # will it have empty string?
    # will it have unicode?
    # if there's special char, what do you want me to do with them?

# RETURN: 
    # return value: boolean. 

# EXAMPLE:
    # Example Do simple examples.
        # Input: s = "anagram", t = "nagaram"
        # Output: True

        # Input: s = "anagram", t = "nagam"
        # Output: False

        # Input: s = "seal", t = "meal"
        # Output: False

# PARAMETER:
    # 1. create a dictionary. key = letter. value = count

    # 2. loop through s. Create a dictionary.
    #     EX: {a:3, n:1, g:1, r:1, m:1}

    # 3. loop through t. if in dictionary, decrement the count.
        # a. check if letter in t is NOT in dictionary, then return False.
  
    # 4. if the value in dictionary reaches 0. just delete that key value pair

    # return true if dictionary is empty. 
    # return false if dictionary is NOT empty

# Method 1: Using hashmap. Increment with s. decrement with t

        d = {}

        for letter in s:
            d[letter] = 1 + d.get(letter, 0) # EX: {a:3, n:1, g:1, r:1, m:1}
        
        for letter in t:
            # if letter in t is NOT in dictionary.
            if letter not in d:
                return False
            # if letter in t IS in dictionary.
            d[letter] -= 1
            if d[letter] == 0:
                del d[letter]


        return not d # Return TRUE if dictionary is empty (false)

# Time: O(S + T) -> O(N)
# Space: O(N)



# METHOD 2: (Not ideal, interviewers might want to see more)
        s = sorted(s) 
        t = sorted(t)

        return s == t
        
# Time: O(NlogN): Slow due to sorting method. sorted() uses timsort which is nlogn
# Space: O(1)

# ---------------------------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# # "eat" = "aet"
# # "tea" = "aet"
# # "tan" = "ant"

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        #  create a list with 26 0s.

        # dictionary: {(0, 0, 0, 0, 0...) aet:"eat", "tea"} 
        # key = tuple of 0s 26 count.
        # # if I'm looking at string= "ac"
        # # (1, 0, 1, 0, 0, 0, ...)
        # ASCII 
        # 'a' = 97
        # 'o' = 111
        # ascii'o' - ascii'a' = 14 
        # at the index of 14, is where the letter 'o' is. 

        # append each word to the tuple that it belongs to.
        # return dictionary.values() 

        # [[asdf], [asdf, asdf]]


        d = {}

        for word in strs: 
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] += 1 

            d.setdefault(tuple(count), []).append(word)

        return d.values()

# Time: O(M * N * 26) OR O(M * N): M is the total number of input strings. N is the average length of a string. 26 is the length of the count array.
# Space: O(N): Since we are using a hashmap.


## METHOD 2: Using Dict and Sort. O(M * N log N) (slower)
        # d = collections.defaultdict(list) # Create an empty dictionary with [] as default.

        ## KEY: sorted word. VALUE: all anagrams of that word.
        dict = {}

        for word in strs:
            dict_key = "".join(sorted(word)) # "".join(['a', 'r', 't'])
            
            if dict_key in dict:  # {"aet":["eat", "tea"], "ant":["tan"]}
                dict[dict_key].append(word)
            else:
                dict[dict_key] = [word]
                
        return dict.values() # Just getting values/keys from dict will be in an array.

# Time: O(M * N log N): M is the number of strings in the input array. N is the length of the longest string and NlogN is the sorting operation and we do it N times.
# Space: O(N): Since we are using a hashmap

# ---------------------------------------------------------------------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:

## Method 1: Two pointers O(N)
        l, r = 0, len(s) - 1
        
        ## Loop until L<R. Loop continues to repeat until isalnum()
        while l < r:

            ## get rid of all NON characters and numbers
            if not s[l].isalnum():
                l += 1
                continue  # move past the NON alnum

            if not s[r].isalnum():
                r -= 1
                continue  # move past the NON alnum

            ## compare lower-cased letters on both sides
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

    ## IF YOU CAN'T USE .iaalnum(), you can just create a method in the class to use.
'''
self.alphaNum(s[l])
        
def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c)<= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
'''

# Time: O(N): Iterates the string once.
# Space: O(1): No extra space used

## Method 2: with python shortcuts. O(N)

        newStr = ""

        # Iterate through input, if alpha/num, += to string
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1] # Returns True of reverse newStr matches regular newstr

# Time: O(N): Iterates once. and compare using reverse slicing is ALSO O(N)
# Space: O(N): new string is proportional to the input S

# ---------------------------------------------------------------------------------


class Solution:
    def firstUniqChar(self, s: str) -> int:

## Create hashMap with counters. Iterate through input until you find a unique letter.

        for char in s:
            d[char] = 1 + d.get(char, 0)
    
        ## Iterate through input and if unique is found, return index
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
   
        return -1

# Time: O(N): Iterate through loop twice. Once to create the dicitonary, once to find unique letter
# Space: O(N): Using hashmap.

# ---------------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------------























"""
Code to share:
"""

# PARAMETER:
# Will the list have only integers? Yes.
# Guaranteed that answer is unique.
# Can list be empty? No.
# Will target ever be 0? No
# Will nums array have enough int for k amount? EX: nums = [1, 1, 2] k = 4

# RETURN VALUE:
# list of integers.

# EXAMPLES:

# Input: nums = [1,1,1,1,2,2,3,4,4,4], k = 3
        # dictionary = {1:4, 2:2, 3:1, 4:3}
        # BEFORE SORT:
        # If the dictionary was a list, it would look: [1, 2, 3, 4]
        # AFTER SORT:
        # sort by dictionary value. least to greatest: [3, 2, 4, 1]
        # 
# Output: [1,4,2]

# PSEUDOCODE: 
    # Look at each element in the array. find the count.
        # dictionary = key:integer, value:count
    # find the integer with the most count and append to list. Do this k amount of times.
    # Using sorted method. we can sort a dictionary by its values. Then use slicing to get exactly the result we want.

        d = {}

        for i in range(len(nums)):
            d[nums[i]] = 1 + d.get(nums[i], 0)

        result = sorted(d, key=d.get)[-k:]  # [3, 2, 4, 1] Sorted least to greatest. Grabs last k elements.

        # top_k = sorted(d, key=d.get, reverse=True)[:k]  # [1, 4, 2, 3] Sorted greatest to least. Grabs first k elements. 

        return result    

# Time: O(N log N): We are sorting(logN) the list N times.
# Space: O(N): since we are using a dictionary.

# ----------------------------------------------------------------------------------------------