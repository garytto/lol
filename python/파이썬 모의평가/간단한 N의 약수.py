# 소인수 분해 구현하면될듯?

number = int(input())

num = 0

numberlist = []
numberlist.append(number)

for i in range(1, 10):
    if number % i == 0:
        numberlist.append(i)
numberlist.sort()

for i in range(len(numberlist)):
    for num in range(1, number):
        if number % (numberlist[i]*num) == 0:
            tmp = (numberlist[i]*num)
            if tmp not in numberlist:
                numberlist.append(tmp)
numberlist.sort()
print(*numberlist)
# for i in range(1, number):
#     if number % (2*i) == 0:
#         if (2*i) not in numberlist:
#             numberlist.append(2*i)
#             num = 2*i

#     if number % (2*i) == 0:
#         tmp = number % (2*i)
#         if (tmp) not in numberlist and num == 0:
#             num += 1
#             numberlist.append(tmp)

# numberlist.sort()
# print(*numberlist)