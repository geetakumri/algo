import re

string = "The roots of education are bitter, but the fruit is sweet."
pattern = "education"
result = re.search(pattern, string)
start_position = result.start()
print(start_position)
