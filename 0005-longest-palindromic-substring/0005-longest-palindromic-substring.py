class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi  = float('-inf')
        string= ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if maxi < len(s[i:j+1]):
                        string = s[i:j+1]
                        maxi = len(s[i:j+1])
        return string