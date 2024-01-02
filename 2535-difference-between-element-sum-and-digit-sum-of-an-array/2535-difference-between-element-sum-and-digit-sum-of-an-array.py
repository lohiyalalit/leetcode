class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        e_sum = sum(nums)
        nums = list(map(str,nums))
        j = "".join(nums)
        d_sum = 0
        for i in j:
            d_sum += int(i)
            
        return abs(e_sum-d_sum)