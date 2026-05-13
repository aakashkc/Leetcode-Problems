class Solution:
    """provide solution for problem"""


    def palindrome(self,n):
        strtype=str(n)
        return strtype == strtype[::-1]

obj=Solution()




class Solutionii:
    """provide solution for problem"""

    def palindrome(self,n):

        reversed_num=0
        original_value=n

        if n<0 or (n%10 == 0 and n!= 0):
            return False
        while n>0:
            digit=n%10
            reversed_num=reversed_num*10+digit
            n//=10
        return original_value == reversed_num

obj=Solutionii()
print(obj.palindrome(121))



