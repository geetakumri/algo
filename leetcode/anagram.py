from collections import Counter

def anagram(s1,s2):
    char_and_its_count ={}
    for i in s1:
        if i in char_and_its_count:
            char_and_its_count[i]+=1
        else:
            char_and_its_count[i]=1

    for i in s2:
        if i in char_and_its_count and char_and_its_count[i]>0:
            char_and_its_count[i]-=1
        else:
            return False
    
    for char_count in char_and_its_count.values():
        if char_count!=0:
            return False

    return True


def is_anagram(word1,word2):
    return Counter(word1)==Counter(word2)

word1 = 'ahbgrettf'
word2 = 'arethbfgt'

print(is_anagram(word1,word2))
    
print(anagram('gee','eeg'))
print(anagram('god','eeg'))
