class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        first_word = strs[0]
        common = ''
        for i in range(len(first_word)):
            for word in strs:
                if not len(word) > i or word[i] != first_word[i]:
                    return common
            common += first_word[i]
        return common
obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
        # strs = ["flower","flow","flight"]
        # sorted strs = ['flight', 'flow' , 'flower']
''' first_word= 'strs[0]'
        for i in range(len(first_word)): #flight
            for word in words:  ['flight', 'fl' , 'flower']
                if not len(word) >= i and word[i] != first_word[i]: len fl = 2 
                        2 >= 2
                    return common
            common += first_word[i] '''



