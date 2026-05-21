VERY Important DSA Usage

A common trick:

if len(nums) != len(set(nums)):

This checks:

duplicates exist

Example
nums = [1,2,3,1]

if len(nums) != len(set(nums)):
print("Duplicates found")

Because:

list length = 4
set length = 3

One duplicate removed.

Time Complexity
len(set_name)

is:

O(1)

Very efficient.

Important DSA Mindset

Sets are commonly used for:

duplicate detection
fast lookup
uniqueness checking
visited tracking (graphs/BFS/DFS)

You’ll use them constantly in DSA.
