class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == "":
            return 0

        total_count = 0

        def count_individual_substrings(i, j):
            palindrome_count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                palindrome_count += 1
                i -= 1
                j += 1
            return palindrome_count
        
        for i in range(len(s)):
            total_count += count_individual_substrings(i, i)
            if i < len(s) - 1:
                total_count += count_individual_substrings(i, i + 1)
        
        return total_count

