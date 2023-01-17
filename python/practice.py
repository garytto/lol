# a, b = map(int, input().split())
# if a > b:
#     print('>')
# if a < b:
#     print('<')
# if a == b:
#     print('==')

# a = int(input())

# if a <= 100 and a > 89:
#     print('A')
# if a < 90 and a > 79:
#     print('B')
# if a < 80 and a > 69:
#     print('C')
# if a < 70 and a > 59:
#     print('D')
# if a < 60 and a > 0:
#     print('F')

# a = int(input())

# if (a%4 == 0 and a%100 != 0) or a%400 == 0:
#     print('1')
# else:
#     print('0')

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')

# h, m = map(int,input().split())

# num = int(m - 45)
# if num < 0:
#     m = 60 + num
#     h -= int(1)
# if num >= 60:
#     m = int(num - 60)
#     h += int(1)
# if num < 60 and num >= 0:
#     m = num

# # 24시 이상이거나 0시 미만인 경우를 대응
# if h < 0:
#     h = 23
# if h > 23:
#     h = 0

# print(f'{h} {m}')

# h, m = map(int,input().split())
# x = int(input())
# num = [int(x//60),int(x%60)] # 입력 받은 수를 시와 분으로 나눠 저장.
# # 1차 계산
# h += num[0] 
# m += num[1]
# if m >= 60:
#     h += 1
#     m -= 60
# # 24시 이상이거나 0시 미만인 경우를 대응
# if h > 23:
#     h -= 24
# print(f'{h} {m}')

# numcnt = int(input())

# for i in range(numcnt):
#     num = list(input())
#     for j in range(len(num)-1):
#         if num[j]==num[j + 1]: 
#             pass
        
#         elif num[j] in num[j + 2:]:
#             numcnt -= 1
#             break
# print(numcnt)

# num = int(input())
# for i in range(1, 10):
#     print(f'{num} * {i} = {num * i}')

# num = int(input())
# numlist = range(0, num + 1)
# numsum = 0
# for i in range(int(len(numlist))):
#     numsum += numlist[i]
# print(numsum)
# print(sum(numlist))

allprice = int(input()) # 총 가격
buy = int(input()) # 산 물품들
buysum = 0 # 산 물품의 합계를 저장할 곳
for i in range(buy): # 계산
    a, b = map(int, input().split()) 
    buysum += (a * b)
if allprice == buysum: # 비교
    print('Yes')
if allprice != buysum: # 비교
    print('No')
