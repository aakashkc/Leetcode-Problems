class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        charDigit=""
        output=[]
        for i in digits:
            charDigit+=str(i)
        charDigit=int(charDigit)+1
        for i in str(charDigit):
            output.append(int(i))
        return output


class SolutionII(object):
    "this is class"
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            print(i)
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        # digits.insert(0,1)
        # return digits
        return [1]+digits

obj=SolutionII()
print(obj.plusOne([9,9,9,9,9]))
