
# num=int(input("enter a number"))
def ugly(num):
    factors=[]
    if num<=0:
        return False
    if num ==1:
        return True
    for i in range(2,num+1):
        while num > 1:
            if num % i == 0:
                factors.append(True) if i == 2 or i ==3 or i ==5 else factors.append(False)
                num=num//i
            else :
                break
    return all(factors)

# print(ugly(num))

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
        for i in [2,3,5]:
            while n % i == 0:
                    n=n//i
        return n==1

obj=Solution()
print(obj.isUgly(30))


