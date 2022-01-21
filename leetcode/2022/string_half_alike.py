class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first_half = s[:len(s)//2]
        sec_half = s[len(s)//2:]
        vowels = 'aeiouAEIOU'
        count_vowel_first_half =0
        count_vowel_sec_half = 0
        
        for char in first_half:
            if char in vowels:
                count_vowel_first_half +=1
        for char in sec_half:
            if char in vowels:
                count_vowel_sec_half +=1
        
        return True if count_vowel_first_half==count_vowel_sec_half else False