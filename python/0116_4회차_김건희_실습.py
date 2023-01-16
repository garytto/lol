# 1 10039 평균 점수 문제

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# numlist = [a, b, c, d, e]
# for i in range(int(len(numlist))):
#     if numlist[i] < 40:
#         numlist[i] = 40
# print(f'{int(sum(numlist)/int(len(numlist)))}')

# 2 10871 X보다 작은 수

# cnt, Mnum = map(int, input().split())
# numlist = list(map(int, input().split()))
# for i in range(cnt): # 10개 이상 입력된 숫자는 확인 안하기 위해 작성.
#     if numlist[i] < Mnum:
#         print(numlist[i], end=" ")

# 3 2480 주사위 세개

# numlist = list(map(int, input().split()))
# numlist.sort()
# result = 0
# if numlist[0] == numlist[1] and numlist[1] == numlist[2] and numlist[0] == numlist[2]:
#     result = 10000 + (numlist[0] * 1000)
# if numlist[0] == numlist[1] and numlist[1] != numlist[2]:
#     result = 1000 + (numlist[0] * 100)
# if numlist[0] != numlist[1] and numlist[1] == numlist[2]:
#     result = 1000 + (numlist[1] * 100)
# if numlist[0] != numlist[1] and numlist[1] != numlist[2] and numlist[0] != numlist[2]:
#     result =  numlist[2]*100
# print(result)

# 4 10886 0 = not cute / 1 = cute

# Tp = int(input())
# result = []
# for i in range(1, Tp + 1):
#     tmp = int(input())
#     result.append(tmp)
# cal = [0, 0]
# for i in range(int(len(result))):
#     if result[i] == int(0):
#         cal[0] += 1
#     if result[i] == int(1):
#         cal[1] += 1
# if cal[0] > cal[1]:
#     print("Junhee is not cute!") # 아 ㅆ.... 이거 juhee is not cute로 써서 3연 오답이였네... ㅠㅠㅠㅠ
# if cal[0] < cal[1]:
#     print("Junhee is cute!")

# 5 3506 점수계산

numbers = int(input())
cnt = 0
numsum = 0
a = list(map(int,input().split()))

for i in range(0, numbers):
    if a[i] == 1:
        numsum += (1 + cnt)
        cnt += 1
    if a[i] == 0:
        cnt = 0
print(numsum)


