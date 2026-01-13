class Solution(object):
    def containsDuplicate(self, nums):
       return len(nums) != len(set(nums))
   

###Step Of Test - Not Sent in Leetcode###
if __name__ == "__main__":
    finder = Solution()
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    for nums, expected in test_cases:
        result = finder.containsDuplicate(nums)
        assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"
    print("All tests passed.")
        
    