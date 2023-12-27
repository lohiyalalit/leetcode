class Solution:
    def fib(self, n: int) -> int:
        
        ans = [0] * (n+1)
        if n <= 1:
            return n
        else:
            ans[0], ans[1] = 0,1
            for i in range(2,n+1):
                ans[i] = ans[i-1] + ans[i-2]
        
        return ans[n]
        