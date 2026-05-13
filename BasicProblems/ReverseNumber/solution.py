class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        posvalue=abs(x) if x<0 else x
        revnum=0
        while  posvalue>0 :
            digit=posvalue%10
            revnum=revnum*10+digit
            posvalue//=10

        return -revnum if x< 0 else revnum



class SolutionII():
    """ :type x: int
        :rtype: int """

    def reverse(self,x):
        sign=-1 if x<0 else 1
        x=abs(x)
        revnum=0
        while x>0:
            digit=x%10
            # if (revnum > MAX//10 or (revnum == MAX //10 and digit > MAX%10)):
            #     return 0
            if revnum < -(2 ** 31) or revnum > (2 ** 31) - 1:
                return 0
            revnum=revnum*10+digit
            x//=10
        revnum*=sign
        return revnum


obj=SolutionII()
print(obj.reverse(-4452962566855))
