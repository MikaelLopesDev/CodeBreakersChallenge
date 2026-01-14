class Solution(object):
    def isAnagram(self, s, t):     
       if len(s) != len(t):
        return False
       count = {}
       for c in s:
           count[c] = count.get(c,0) + 1
       for c in t:
           if c not in s or count[c] == 0:
                return False
           count[c] -= 1
       return True
               
### algorithmic complexity: O(n)
### Lib of Python that uses the same code behind the scenes: collections.Counter
##  from collections import Counter
##class Solution(object):
##    def isAnagram(self, s, t):
##        return Counter(s) == Counter(t)

   
###Step Of Test - Not Sent in Leetcode###
if __name__ == "__main__":
    checker = Solution()
    test_cases = [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("listen", "silent"), True),
        (("hello", "billion"), False),
    ]

    for (s, t), expected in test_cases:
        result = checker.isAnagram(s, t)
        assert result == expected, f"Test failed for input ({s}, {t}). Expected {expected}, got {result}"
    print("All tests passed.")