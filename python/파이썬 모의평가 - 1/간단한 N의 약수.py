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