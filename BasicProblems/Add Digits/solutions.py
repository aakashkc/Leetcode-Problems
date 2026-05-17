class Solution:
    def addDigit(self,num):
        while num>9:
            tsum=0
            for i in str(num):
                tsum=tsum+int(i)
            num=tsum
        return num

obj=Solution()
print(obj.addDigit(456))


class SolutionII:
    def addDigit(self,num):
        while num>9:
            totalsum=0
            while num>0:
                totalsum+=num%10
                num//=10
            num=totalsum
        return num
obj1=SolutionII()
print(obj1.addDigit(9))









