# DATE: March 8th, 2024
# Week 2

'''
383. Ransom Note (EASY) (HINT: Hash Table)
283. Move Zeroes (EASY) (HINT: Two Pointers)
26. Remove Duplicates from Sorted Array (EASY) (HINT: Two Pointers)
80. Remove Duplicates from Sorted Array II (MEDIUM) (HINT: Two Pointers)

Since we are learning about Stack, Queue, and linked list in CS5001 this week.
Let's try the following:

225. Implement Stack using Queues
232. Implement Queue using Stacks
876. Middle of the Linked List
141. Linked List Cycle I
'''



# ---------------------------------------------------------------------------


383. Ransom Note (EASY)
# TWO ARRAYS GIVEN FIND IF ARRAY1 CAN BE FOUND IN ARRAY2

# Create two dictioanries for both arrays that count each letter.
# Compare ransomNote to magazine by using if statements in a for loop.abs

(Some IDE might require this)
from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Counter(ransomNote) and Counter(magazine) create dictionaries with character counts.
        rn_dict = Counter(ransomNote)
        m_dict = Counter(magazine)

        ## USE THIS if Counter method is not allowed
        '''
        rn_dict = {}
        m_dict = {}
        for n in ransomNote:
            rn_dictN[n] = 1 + n_dict.get(n, 0)
        for n in magazine:
            m_dict[n] = 1 + m_dict.get(n, 0)
        '''

        # For loop checks if each character in `ransomNote` is available in `magazine`
        for key, val in rn_dict.items():
            # If letter in ransomNote is NOT in magazine
            if key not in m_dict:
                return False
            # If letter in ransomNote IS in magazine.
            else:
                # Check if magazine has enough letters for ransomNote.
                if m_dict[key] < val:
                    return False
        # If you loop through all of ransomNote successfully, there is enough letter in magazine.
        return True

# Time Complexity: O(N + M), where N is the length of ransomNote and M is the length of magazine. Counting characters in both strings takes linear time.
# NOTE: When we say O(n + m), it means that the time complexity grows with the sum of the sizes of BOTH inputs. It is diffferent than O(n), O(n) means the time complexity depends on ONE input.
# Space Complexity: O(N + M) for storing character counts of ransomNote and magazine. 


# ---------------------------------------------------------------------------


283. Move Zeroes
# CONSTRAINTS: No need for edge case since we won't have empty list as input.

# NOTE: Whenever I see the instructions, "modify nums in-place". I think of using two pointer approach.
#     Left and right pointer for arrays.
#     Row and column pointer for matrices.

# We will use a l, r two pointer, they both will start at 0.
# Loop until r pointer reaches the end.
# Only r pointer will move when there is a zero. l pointer will wait on zero that needs to be changed.
    # If value at r pointer is NON-ZERO: (What condition are we looking for?)
        # Switch the values at nums[l] and nums[r]
    # Move r pointer at every loop. 
# No need to return anything since we changed the array in-place.

# Follow-up: Coult you minimize the total number of operations done?
# Using two pointer takes care of the follow-up challenge.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, 0

        while r < len(nums):
            # ONLY r pointer will move when there is ZERO.
            # l pointer will only move when you encounter NON-ZERO.
            if nums[r]:  # 0 is False, all non-zero values are True
                # Trading the element in-place between l and r pointer.
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

# Time: O(n): Since we are iterating through nums once.
# Space: O(1): We are modifying the array in-place.


# ---------------------------------------------------------------------------


26. Remove Duplicates From Sorted Array I. (TWO POINTER) 
# CONSTRAINTS: No need for edge case since we won't have empty list as input.

# NOTE: Need to solve it in place O(1). Return K after the final result. INT after K does not matter.
# NOTE: Whenever I see that the constraint says 'sorted in non-decreasing order,' just know that the array will have duplicates and increasing values.

# l, r pointer both start at 1 since we are looking for unique elements. (Only ONE unique element allowed)
# Loop until r pointer reaches the end.
# Only r pointer will move when there is duplicate. l pointer will wait on the duplicate that needs to be changed.
    # If value at r pointer and l - 1 pointer different: (What condition are we looking for?)
        # Change the value at the left pointer to match the value at the right pointer.
        # move l pointer up so that it is waiting on the next potential duplicate.
    # Move r pointer at every loop. 
# Return l pointer. Because it will eventually end up where the final array length should be at.
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # l, r starts at 1. index 0 is considered non-duplicate.
        l, r = 1, 1

        while r < len(nums):
            # ONLY r pointer will move when there is DUPLICATE. 
            # l pointer will only move when you encounter NON-DUPLICATE.
            if nums[r] != nums[l - 1]: # Only ONE unique element allowed.
                # Change the value at l pointer to the value r pointer is at.
                nums[l] = nums[r]
                l += 1
            r += 1
        # l represents length of the final array.
        return l

# Time: O(N): One iteration through the input list.
# Space: O(1): Only uses fixed amount of extra space


# ---------------------------------------------------------------------------


# 80. Remove Duplicates From Sorted Array II (TWO POINTER) 
# CONSTRAINTS: No need for edge case since we won't have empty list as input.

# NOTE: Need to solve it in place O(1). Return K after the final result. INT after K does not matter.
# NOTE: Whenever I see that the constraint says 'sorted in non-decreasing order,' just know that the array will have duplicates and increasing values.

# l, r pointer both start at 2 since we are looking for unique elements. (Only TWO of the same unique elements allowed)
# Loop until r pointer reaches the end.
# Only r pointer will move when there is duplicate. l pointer will wait on the duplicate that needs to be changed.
    # If value at r pointer and l - 2 pointer different: (What condition are we looking for?)
        # Change the value at the left pointer to match the value at the right pointer.
        # move l pointer up so that it is waiting on the next potential duplicate.
    # Move r pointer at every loop. 
# Return l pointer. Because it will eventually end up where the final array length should be at.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ## l, r starts at 2. Until Index 1 is considered non-duplicate.
        l, r = 2, 2
        
        
        while r < len(nums):
            # ONLY r pointer will move when there is DUPLICATE. 
            # l pointer will only move when you encounter NON-DUPLICATE.
            if nums[r] != nums[l - 2]: # Only TWO of the same unique elements allowed.
                nums[l] = nums[r]
                l += 1
            r += 1
        # l represents length of the final array. 
        return l 

        
# Time: O(N): One iteration through the input list.
# Space: O(1): Only uses fixed amount of extra space


# ---------------------------------------------------------------------------


225. Implement Stack using Queues
# I will just go ahead and use a single queue to solve this instead of double. (follow-up question)
## NOTE: The reason we are using deque instead of list to implement a queue is because of time complexity. using insert() and pop() on the left will result in time complexity of O(N). However with deque() we can use it like a queue and it is only a constant time complexity O(1). deque() is also thread safe so you don't have to worry about collision.

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int: # We will be grabbing elements from the left and putting it back on the right.
        for i in range(len(self.q) - 1): # Loop until the last number.
            self.push(self.q.popleft()) # We are only able to popleft since we are using queue.
        return self.q.popleft() 

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
        

# # Time: O(N): Since we are using a queue to pop(), it makes the time complexity O(N).
# # Space: O(1)

# List and deque: append and pop at the RIGHT will have O(1)
# List: append/insert and pop at the LEFT will have O(N) unlike deque that has O(1). List takes longer due to repositioning of all elements after.
# Deque: append and pop at the LEFT will have O(1).

# The time complexity explanation for the method pop()
# Having pop and append from left of list IN A FOR LOOP will result in time O(N^2). But since we are using Queue in a forloop, it is O(N)


# ---------------------------------------------------------------------------

232. Implement Queue using Stacks

class MyQueue:
    def __init__(self):
        # Stacks for pushing to and popping from the queue
        self.stack_pusher = [] 
        self.stack_popper = [] 

    def push(self, x: int) -> None:
        # Push an element into the queue
        self.stack_pusher.append(x)

    def pop(self) -> int:
        # Ensure stack_popper has elements, then pop
        self.prepare_stack_popper()
        return self.stack_popper.pop()

    def peek(self) -> int:
        # Ensure stack_popper has elements, then peek
        self.prepare_stack_popper()
        return self.stack_popper[-1]

    def empty(self) -> bool:
        # Check if queue is empty
        return len(self.stack_popper) + len(self.stack_pusher) == 0

    def prepare_stack_popper(self) -> int:
        # Move elements from stack_pusher to stack_popper if needed
        if not self.stack_popper:
            while self.stack_pusher:
                self.stack_popper.append(self.stack_pusher.pop())

# Time Complexity:
# Worst-case O(n): This happens during pop or peek when we have to move all items from one stack_pusher to stack_popper. If there are n items, we touch each one, so it takes n steps.
# Amortized O(1): "Amortized" means averaged over many operations. Most times, pop and peek are quick (just removing the top item of a stack), but occasionally we spend time moving items between stacks. Spread out over many operations, the time spent per operation is small, like it's O(1) on average.

# Space Complexity: O(n) for storage of elements across both stacks


# ---------------------------------------------------------------------------

876. Middle of the Linked List

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers at the start.
        slow, fast = head, head

        # Loop until 'fast' or 'fast.next' is None.
        while fast and fast.next:
            slow = slow.next  # Move 'slow' one step.
            fast = fast.next.next  # Move 'fast' two steps.
        return slow  # 'slow' is now at the middle.

# Time: O(N) - because we traverse the list once.
# Space: O(1) - because we use fixed space regardless of input size.


# ---------------------------------------------------------------------------


Slow and fast pointer is one of the patterns we need to recognize. (A.K.A. Floyd's Tortoise and Hare Algoirthm)
This is a pattern where Fast pointer travels twice as fast as the Slow pointer.
It's very useful when dealing with any cyclic linked lists or arrays!

It's a similar concept to Sliding Window and Two Pointers patterns we will learn eventually. 

Here is another easy linked list leetcode question that uses slow and fast pointers.

141. Linked List Cycle I (SLOW, FAST POINTER)
# LINKED LIST GIVEN. FIND IF THERE IS A CYCLE. RETURN TRUE IF THERE IS CYCLE.
# If there’s a loop, fast catches up to slow, proving a cycle. If not, fast reaches the end first, showing there’s no cycle.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Slow and Fast pointers are both starting at head (beginning)
        slow, fast = head, head

        # We need the condition fast and fast.next.
        # Avoid Errors: It ensures fast isn't at the list's end and can safely move
        # two steps ahead without causing an error from trying to access a non-existent next node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Time: O(N): Iterates through array once.
# Space: O(1): Only uses constant amount of extra space