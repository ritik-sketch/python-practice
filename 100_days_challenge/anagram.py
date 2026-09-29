#give a string write a sunction to check if it is an anagram of another string 

''''
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)
srt1 = 'listen'
str2 = 'silent'
print(anagram(srt1,str2))
'''

def is_anagram(s,t):
    if len(s) != len(t):
        return False 
    count_s = {}
    for ch in s:
        if ch in count_s:
            count_s[ch] = count_s[ch]+1
        else:
            count_s[ch] = 1
    count_t = {}
    for ch in t:
        if ch in count_t:
            count_t[ch] = count_t[ch] +1
        else:
            count_t[ch]=1
    return count_s == count_t 

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))