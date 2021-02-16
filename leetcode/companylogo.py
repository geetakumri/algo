'''import collections
from collections import Counter
company_name = input('enter the company name')
#company = sorted(company_name)
#counts = Counter(company)
lst = []
for i in company_name:
    lst.append(i)
print(lst)
occurrences = collections.Counter(lst)

for i in occurrences :

print('occurences',occurrences)
for i in company:
    print(i,counts[i])'''

from collections import Counter
[print(*k) for k in Counter(sorted(input())).most_common(3)]