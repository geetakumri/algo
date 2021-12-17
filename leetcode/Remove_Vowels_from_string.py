
    def remove_vowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        new_string = ""
        for letter in range(len(S)):
            if S[letter] not in vowels:
                new_string += S[letter]
        return new_string


def remove_vowels(param):
    pass


remove_vowels('geeta')