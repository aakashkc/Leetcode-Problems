"""dfawef"""

numb = int(input("enter number"))
# for i in range(num + 1):
#     lst = ""
#     while i >= 1:
#         if i % 2 == 0:
#             lst = "0" + lst
#             i //= 2
#         else:
#             lst = "1" + lst
#             i //= 2
#     ans.append(lst.count("1"))
ans = []
for i in range(numb + 1):
    count = 0
    num = i
    while num > 0:
        if num % 2 == 1:
            count += 1
        num //= 2
    ans.append(count)
print(ans)
