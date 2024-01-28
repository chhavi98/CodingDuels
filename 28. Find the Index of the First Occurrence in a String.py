class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
obj = Solution()
print(obj.strStr("sadbutsad" , "sad"))
'''
        len(needle) > len(haystack)
        return -1
#abc  c
 123. 1

        for i in range(len(haystack)- len(needle))
            if haystack[i:i+len(needle)] == needle
                return i

        '''
