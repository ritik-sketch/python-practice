#You are given a list of strings. Write a function to filter out all strings that are palindromes.
'''
def isPalindrome(str):
    str = str.lower()

    reversed_str = str[::-1]
    return str == reversed_str
print(isPalindrome("Madam"))
print(isPalindrome("Ritik"))
'''
''''
def filter_non_palinfromes(strings):
    result = []
    for s in strings:
        s_lower = s.lower()
        reversed_s = s_lower[::-1]

        if s_lower != reversed_s:
            result.append(s)
    return result
words = ["Madam", "hello", "Level", "python"]
filtered = filter_non_palinfromes(words)
print(filtered)
'''
#एक string दी गई है, उसमें से सबसे लंबा palindrome ढूंढो — पूरा string palindrome नहीं है, बस substring हो सकती है

#--s = "babad"
#--output: "bad" or "aba"
'''
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]  # valid palindrome substring

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome (center at i)
        p1 = expand_around_center(i, i)
        # Even length palindrome (center between i and i+1)
        p2 = expand_around_center(i, i+1)

        # Update longest if needed
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2

    return longest
s = "babad"
print(longest_palindrome(s))
'''






#Number को string में convert किए बिना check करो कि वो palindrome है या नहीं


n = 121  # You can change this value to test other numbers
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")



s= "madam"
if s == s[::-1]:
    print("palindrom")
else:
    print("not palimdrome")