Yes — this problem has a famous mathematical solution called:

Digital Root

Instead of repeatedly summing digits,
we can compute the answer directly in:

O(1)

time.

Pattern

digital root=1+(n−1)mod9

Final O(1) Solution
class Solution(object):

    def addDigits(self, num):

        if num == 0:
            return 0

        return 1 + (num - 1) % 9

Example
Input
38
Calculation
1 + (38 - 1) % 9

↓

1 + 37 % 9

↓

1 + 1

↓

2

Correct answer.

Why This Works

This comes from a mathematical property:

Numbers repeat their digit sums every 9.

Example:

Number Digit Sum
9 9
18 1+8=9
27 2+7=9
36 3+6=9

All multiples of 9 reduce to 9.

Another Example
123

↓

1 + 2 + 3 = 6

Also:

1 + (123 - 1) % 9

↓

1 + 122 % 9

↓

6
Important Edge Case

If:

num = 0

formula breaks because:

1 + (-1 % 9)

So we handle:

if num == 0:
return 0
