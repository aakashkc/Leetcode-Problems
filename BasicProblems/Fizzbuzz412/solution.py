# self solved
class Solution:
    """provide solution for problem"""

    def hello(self):
        """just to escape pylint error"""
        return None

    def fizzbuzz(self, n):
        """return fizzbuzz problems solution"""
        lst = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                lst.append("FizzBuzz")
            elif i % 3 == 0:
                lst.append("Fizz")
            elif i % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        return lst


obj = Solution()
print(obj.fizzbuzz(15))

# Better DSA Version


class SolutionII:
    """provide solution for problem"""

    def hello(self):
        """just to escape pylint error"""
        return None

    def fizzbuzz(self, n):
        """return fizzbuzz problems solution"""
        result = []
        for i in range(1, n + 1):
            current = ""
            if i % 3 == 0:
                current += "Fizz"
            if i % 5 == 0:
                current += "Buzz"
            if current == "":
                current = str(i)
            result.append(current)
        return result


objii = SolutionII()
print(objii.fizzbuzz(10))
