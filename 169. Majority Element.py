import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        count_dict = collections.Counter(nums)
        print(sorted(count_dict, key=count_dict.get, reverse = True))
        p = sorted(count_dict, key=count_dict.get, reverse = True) [0:1]
        return p[0]
obj = Solution()
print(obj.majorityElement([1,2,2,2,2,3]))