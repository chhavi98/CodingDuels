class Solution:
    def merge(Self,nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[::] = sorted(nums1[:m] + nums2[:n])
        print(nums1)
obj = Solution()
obj.merge([1,2,3,0,0,0], 3,[2,5,6], 3)



