class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev = str(num)
        if (len(rev)>0) and (int(rev[-1]) !=0):
            return True
        elif(num==0):
            return True
        else:
            return False