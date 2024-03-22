# DATE: March 22nd, 2024
# Week 2

'''
349. Intersection of Two Arrays (Easy)
350. Intersection of Two Arrays II (Easy)
11. Container With Most Water (Medium)
127. Word Ladder (HARD)
'''

349. Intersection of Two Arrays (EASY)

(HASHMAP/ARRAY) COMPARE TWO ARRAYS. SOLUTION HAS NO DUPLICATES

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Create dictionary for nums1.
        # Key: Integer Value. Value: Boolean
        d = {}
        for n in nums1: 
            d[n] = True

        # Loop through nums2. 
        # If numbs from num2 exists, add to res = []
        # Then del d[n] since we don't want duplicate answer.
        res = []
        for n in nums2:
            if n in d:
                res.append(n)
                del d[n]
        return res

# Time: O(N + M): N is nums1 and M is nums2
# SPace: O(N): Using dictionary and list.


# ---------------------------------------------------------------------------


350. Intersection of Two Arrays II (EASY)

(HASHMAP/ARRAY) COMPARE TWO ARRAYS. SOLUTION HAS DUPLICATE


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Create dictionary for nums1.
        # Key: Integer Value. Value: Count of the value
        d = {}
        for n in nums1: 
            d[n] = 1 + d.get(n, 0)

        # Loop through nums2. 
        # If nums2 also exists in nums1, add to res = []
        # del d[n] only AFTER counter reaches 0 since we want duplicate answer.
        res = []
        for n in nums2:
            if n in d: 
                res.append(n)
                d[n] -= 1
                # ONLY delete once it reaches zero since we allow duplicate integers for solution.
                if d[n] == 0:
                    del d[n]
        return res

# Time: O(N + M): N is nums1 and M is nums2
# SPace: O(N): Using dictionary and list.  


# ---------------------------------------------------------------------------


11. Container With Most Water (Medium)
(TWO POINTER)
# NOTE: Does not matter how HIGH height is. You will be using LOWER height to calculate area.

# have left and right pointer. left at beginning, right at end.
# calculate the rectangle by min(l,r) * (r-l)
    # You use the smaller value between Left and Right because "water will spill out" and the maximum water it can hold will be determined by lower bar.
# move the height that is lower (l or r)
# keep track of the highest area.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            max_area = max(area, max_area)
        
        return max_area

# Time: O(N): Looping through the given array once.
# Space: O(1): Only using constant amount of space.


# ---------------------------------------------------------------------------


127. Word Ladder (BFS). WORD WITH HASHMAP OF POSSIBLE OTHER WORD COMBINATION

# Use nested for loop to append to hashmap with patterns as key and words as values. {*ot : [hot, dot, lot]}
# Iterate through the q, keep track of visited and return res if you reach the endWord.
# 
# Constraints: 
    # Length of word will be <= 10.
    # Length of word LIST will be <= 5000
# hot -> *ot, h*t, ho*
# dot -> *ot, d*t, do*
# {*ot : [hot, dot, lot]}
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ## Edge Case. 
            ## Make sure endWord is in the wordList.
        if endWord not in wordList:
            return 0

        nei = defaultdict(list) # default []
        ## ** IF beginWord is NOT in the wordList.
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:] # hot -> *ot, h*t, ho*
                nei[pattern].append(word) # {*ot: hot}

        ## Use set to make sure we don't visit the word twice.
        visit = set([beginWord]) # add beginWord so that we don't visit it again.
        q = collections.deque([beginWord])
        res = 1 # because we have at least one word (beginWord)
        
    
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:] # grab the pattern of the word to look through hashmap
                    for neiWord in nei[pattern]: # Getting the values {*it: sit, kit, mit}
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

#  Time: (O(N * M^2))
# Create Adjacency List (O(NM^2)): Going through every word is N. Go through every char to replace with '*' is M. Then adding each word to the list is another M.
# Space: O(N * M): Hashmap has M length of each word in patterns. Each pattern has N number of words in wordList