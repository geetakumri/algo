# to find whether the a character is occurring more than 50% in a sentence

input_string = input('enter a sentence')
count = 1
max_occur_char = input_string[0]
for i in range(1, len(input_string)):
    if max_occur_char != input_string[i]:
        count -= 1
        if count == 0:
            max_occur_char = input_string[i]
            count += 1
    else:
        count += 1
print(f'character with maximum frequency is {max_occur_char}')
