class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        l = 0
        num = n
        num = int(str(n)[::-1])
        #print(num)
        
        s = 0
        while num:
            if l%2==0:
                s += num%10

            else:
                s -= num%10

            num = num//10
            l += 1
            
        return s