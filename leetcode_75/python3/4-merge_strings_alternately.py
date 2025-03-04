# Merge the words alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for x,y in zip(word1, word2):
            result.append(x)
            result.append(y)
        
        # Add the rest of the longer word.
        result.append(word1[len(word2):]) or result.append(word2[len(word1):])

        return ''.join(result)

sol = Solution()
print(sol.mergeAlternately("abc", "xyz"))