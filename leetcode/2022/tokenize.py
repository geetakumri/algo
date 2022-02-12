from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import ast, sys

sentence = sys.stdin.read()
sentence = sentence.lower()

words = word_tokenize(sentence)
stopwords = stopwords.words("english")
no_stops = [word for word in words if word not in stopwords]
print(len(no_stops))
