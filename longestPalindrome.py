class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        current = ''
        if(len(s) == 0):
            return current
        else:
            max_len = 1
            current = s[0]
        for i in range(len(s)):
            for j in range(i+max_len,len(s)):
                if(s[i] == s[j]):
                    if((j-i+1) > max_len):
                        if(checkForPalindrome(s[i:j+1])):
                            current = s[i:j+1]
                            max_len = j-i+1
        return current
    
def checkForPalindrome(string):
    isPalindrome = True
    for index in range(len(string)//2):
        if(string[index] != string[-(index+1)]):
            isPalindrome = False
    return isPalindrome
            