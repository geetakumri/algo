import requests
from nltk import FreqDist

url = "https://www.gutenberg.org/files/16/16-0.txt"

peter_pan = requests.get(url).text
peter_pan_words = peter_pan.split()
word_frequency = FreqDist(peter_pan_words)
print(word_frequency.most_common)
# extract the  third most frequent word
word = word_frequency.most_common(3)[2][0]
# extract the frequency of third most frequent word
freq = word_frequency.most_common(3)[2][1]
print(f"The third  most  frequent word is '{word}'with frequency {freq}")
