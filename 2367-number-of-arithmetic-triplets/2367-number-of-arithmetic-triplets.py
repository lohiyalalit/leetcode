class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n, res = len(nums), []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        res.append([i,j,k])
                    
        return len(res)