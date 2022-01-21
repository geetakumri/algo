class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output_lst = []
        sum =0
        for i in nums:
            sum+=i
            output_lst.append(sum)
        
        return output_lst