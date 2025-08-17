class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for  index, num in enumerate(nums, start=0):
            for index2, num2 in enumerate(nums, start=0):
                if not index == index2:
                    if (num+num2) == target:
                        return [index,index2]



if __name__ == '__main__':
    solution = Solution().two_sum([2, 7, 11, 15], 9)
    print(solution)