# import sys
# input = sys.stdin.readline

# # 2576 홀수
# numbers = []
# cnt = 0

# for i in range(7): # 7개의 숫자 입력 받음
#     num = int(input())
#     if num%2 != 0:
#         numbers.append(num)
#         cnt += 1

# if cnt > 0:
#     print(sum(numbers))
#     print(min(numbers))

# else:
#     print(-1)

# 10822 더하기
# numbers = list(map(int, input().split(',')))
# print(sum(numbers))

# 2754 학점계산
# score = {'A+': '4.3', 'A0': '4.0', 'A-': '3.7'
# ,'B+': '3.3', 'B0': '3.0', 'B-': '2.7','C+': '2.3', 'C0': '2.0', 'C-': '1.7'
# ,'D+': '1.3', 'D0': '1.0', 'D-': '0.7','F': '0.0'}
# n = input().rstrip()
# print(score[n])

# 5622 다이얼 - 1 번 풀이
# n = input().rstrip()
# result = 0
# for i in n:
#     if i in 'ABC':
#         result += 3
#     elif i in 'DEF':
#         result += 4
#     elif i in 'GHI':
#         result += 5
#     elif i in 'JKL':
#         result += 6
#     elif i in 'MNO':
#         result += 7
#     elif i in 'PQRS':
#         result += 8
#     elif i in 'TUV':
#         result += 9
#     else:
#         result += 10
# print(result)

# 5622 다이얼 - 2 번 풀이
# n = input().rstrip()
# numbers = {'ABC': int(3), 'DEF': int(4),'GHI': int(5),'JKL': int(6),'MNO': int(7),'PQRS': int(8),'TUV': int(9),'WXYZ': int(10)}
# result = 0
# for i in numbers.keys(): ## key값을 i로 받아옴.
#     for j in n: # 입력받은 n을 하나 하나 j에게 받아옴
#         if j in i: # keys에서 받은 i의 값에 j가 들어가있다면.
#             result += numbers[i] # 관련 키의 value 값을 result에 넣어준다.
#         else: # pass를 넣으면 시간이 좀더 단축됨. 해당 내용 공부 필요함. 정확하게 왜 필요한지를 모르겠음.
#             pass
# print(result)

# 2577 숫자의 개수
# A = int(input())
# B = int(input())
# C = int(input())
# numbersum = str(A*B*C)
# number = {}
# for i in range(10):
#     n = str(i) # ㅎㅎ 키값이 문자열이라서 한번 변환해줘야되네 히히히히ㅣㅎ히히히히ㅣ히히히히
#     number[n] = 0

# for i in numbersum:
#     if i in number:
#         number[i] += 1
# for i in number:
#     print(number[i])

# 7785 회사에 있는 사람

N = int(input())
person = {}

for n in range(N):
    a, b = input().rstrip().split()
    if a not in person:
        person[a] = b
    elif a in person:
        del(person[a])

personlist = sorted(person, reverse=True)
# print(*personlist)
for i in personlist:
    print(i)
