
def getGenomeSeq(seq):
    prevSeq, currSeq = seq[0], None
    result = prevSeq
    for i in range(1, len(seq)):
        currSeq = seq[i]
        result += partOfSeqNotPresent(prevSeq, currSeq)
        prevSeq = currSeq
    return result

def partOfSeqNotPresent(prevSeq, currSeq):
    left, right = int(0), len(currSeq)
    while(left < right):
        if currSeq[left:right] not in prevSeq:
            right -=1
        break;
    return currSeq[right:len(currSeq)]

seq = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]

print(getGenomeSeq(seq))

# Program to check Armstrong numbers in a certain interval

lower = 1
upper = 2000

for num in range(lower, upper + 1):

    # order of number
    pow = len(str(num))

    # initialize sum
    sum = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        sum += rem ** pow
        temp //= 10

    if num == sum:
        print(num)