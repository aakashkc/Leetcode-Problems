class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n%2 == 0:
            n/=2
        return n==1


# solution using bit manipulation

class SolutionII(object):
    def isPowerOfTwo(self, n):
        return n>0 and n&(n-1)==0

