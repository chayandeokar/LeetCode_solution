# Binary-search-Algo


# https://leetcode.com/problems/binary-search/
 
******************************************************************************
 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1                         
            else:
                right = mid - 1
        
        return -1
     
**********************************************************************************
# Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

# Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse
