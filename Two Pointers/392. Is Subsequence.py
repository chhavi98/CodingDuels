class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            t = t[i+1:]
        return True
obj = Solution()
res = obj.isSubsequence('abc', 'ahbgdc')
print(res)