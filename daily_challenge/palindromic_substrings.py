# Problem Link : https://leetcode.com/problems/palindromic-substrings/
# Video Link : https://www.youtube.com/watch?v=PHrUviz47kY

# Given a string s, return the number of palindromic substrings in it.

class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            #  for odd length palindromes
            palindromes = palindromes + self.get_palindromes(s, i, i)
            #  for even length palindromes
            palindromes = palindromes + self.get_palindromes(s, i, i+1)
        return palindromes
    
    def get_palindromes(self, s, i, j):
        count = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        return count
        
        

        
