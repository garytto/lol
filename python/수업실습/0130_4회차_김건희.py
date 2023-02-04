# 1225 이상한 곱셈
import sys
input = sys.stdin.readline
# a, b = input().rstrip().split()
# c = []
# d = []

# for i in range(len(a)):
#     c.append(int(a[i]))
# for i in range(len(b)):
#     d.append(int(b[i]))
    
# print(sum(c)*sum(d))

#2438 별

# N = int(input())

# for i in range(1, N+1):
#     print('*'*i)

# 2739 구구단

# num = int(input())
# for i in range(1, 10):
#     print(f'{num} * {i} = {num * i}')

# 2953 나는 요리사다.
# list_list = []
# mNum = 0
# index = 0
# for i in range(5): # 5줄
#     list_list.append(list(map(int, input().split()))) # 리스트로 값 저장
#     if mNum < sum(list_list[i]):
#         index = i + 1 # i는 0 부터시작 순서는 1부터 시작
#         mNum = sum(list_list[i])
# print(index, mNum)

# 2669 직사각형 네개의 합집합의 면적 구하기

board = [[0 for _ in range(101)] for _ in range(101)] # 공간 좌표 생성.
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1 # 보드에 색칠하기. += 쓰면 안됨. 만약 중복 되는 경우에는 2가 되기에. 그저 1로 해둬서 중복인 경우 의미 없는 행동을 하기 위해 1로 "바꾼다"의 개념으로 = 사용.

for n in board:
    result += sum(n) # board에 색칠 되어 있는 아이들 합 더하기.(1로 지정해둔 아이들.) 보드에 사각형이 있다면 최소 면적 값이 1이기에 1로 단위지정함. 만약 2라면 위에 2로 바꾸면됨.

print(result)
