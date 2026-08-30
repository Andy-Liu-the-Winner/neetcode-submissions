class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char for char in s if char.isalnum()).lower()
        return text == text[::-1]