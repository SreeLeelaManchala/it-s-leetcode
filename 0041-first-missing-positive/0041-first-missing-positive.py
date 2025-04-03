class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res=1
        for num in nums:
            if num<0:
                continue
            elif num==res:
                res+=1
            elif num>res:
                break
        return res
        