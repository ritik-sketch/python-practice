#give a string write a sunction to check if it is an anagram of another string 


def anagram(s1, s2):
    return sorted(s1) == sorted(s2)
srt1 = 'listen'
str2 = 'silent'
print(anagram(srt1,str2))