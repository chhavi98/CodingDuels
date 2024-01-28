class Solution:
    def reverseWords(self, s: str) -> str:

        l = s.split()
        l = l[::-1]
        return ' '.join(l)
obj = Solution()
print(obj.reverseWords("the sky is blue"))