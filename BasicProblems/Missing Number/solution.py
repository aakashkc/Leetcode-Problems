nums=[0,1,2,3,4,6]

class Solution:
    def missing_number(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i



class Solution:
    def missing_number(self, nums):
        total_number=len(nums)
        expected_total=total_number*(total_number+1) //2
        actual_total =sum(nums)
        return expected_total-actual_total




obj=Solution()
print(obj.missing_number(nums))
