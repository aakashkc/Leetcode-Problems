n&(n-1)==0. what is this in python
12:34 AM

Recognized bit manipulation operation for power-of-two checking
Recognized bit manipulation operation for power-of-two checking
This is a bit manipulation trick to check if a number is a power of 2.

How it works
python
n & (n-1) == 0
& is the bitwise AND operator — it compares bits of two numbers.

The trick works because powers of 2 in binary always look like:

1 → 0001
2 → 0010
4 → 0100
8 → 1000
And n-1 always flips all the bits after the leading 1:

8 → 1000
7 → 0111
8 & 7 = 0000 ✅ power of 2
Compare with a non-power of 2:

6 → 0110
5 → 0101
6 & 5 = 0100 ❌ not zero, not a power of 2
In code
python
def isPowerOfTwo(n):
return n > 0 and (n & (n - 1)) == 0

print(isPowerOfTwo(8)) # True
print(isPowerOfTwo(6)) # False
print(isPowerOfTwo(1)) # True
⚠️ Always add n > 0 check — because 0 & -1 == 0 would wrongly return True for zero.

Why it matters for DSA
This is a classic bit trick that appears frequently in interviews. The key patterns to know:

Trick What it does
n & (n-1) == 0 Check power of 2
n & 1 Check if odd or even
n >> 1 Divide by 2
n << 1 Multiply by 2
Good that you're encountering these early — bit manipulation is a whole topic on its own in DSA.

Claude is AI and can make mistakes. Please double-check responses.
