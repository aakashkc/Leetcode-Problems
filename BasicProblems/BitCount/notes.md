The main improvement now is:

avoid unnecessary string operations
learn patterns behind bit manipulation
reduce repeated work

Your Current Approach
num = int(input("enter number"))
ans = []

for i in range(num + 1):
lst = ""
while i >= 1:
if i % 2 == 0:
lst = "0" + lst
i //= 2
else:
lst = "1" + lst
i //= 2
ans.append(lst.count("1"))

print(ans)
Problems in Current Code

1. You are modifying i

Inside the while loop:

i //= 2

You destroy the loop variable.

Very dangerous habit in DSA/interviews.

Always use another variable.

2. Building binary strings is expensive
   lst = "1" + lst

String concatenation repeatedly is costly.

You do not actually need the binary string.

You only need the count of 1.

3. Repeated work

For every number:

convert to binary
count ones

This repeats many computations.

DSA optimization often means:

reuse previous computations
