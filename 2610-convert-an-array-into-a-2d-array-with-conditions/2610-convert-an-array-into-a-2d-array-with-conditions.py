class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        temp = defaultdict(int)
        max_row = 0
        for i in nums:
            temp[i] += 1
            max_row = max(max_row, temp[i])
            
        res = [[] for _ in range(max_row)]    
        cur_count = 0
        for i in temp:
            count = temp[i]
            cur_row = 0
            while count > 0:
                res[cur_row].append(i)
                cur_row += 1
                count -= 1

        return res