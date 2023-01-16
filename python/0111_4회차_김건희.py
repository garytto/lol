# 문제 1

# number = list(map(int,input().split()))

# print(*number)

# 문제 2

# import sys
# sys.stdin = open("input.txt", "r")

# print(*sys.stdin)

# 문제 3

# TC = int(input('TC의 갯수를 입력하시오 > '))

# for tc in range(1, TC + 1):
#     Num = int(input('줄 수를 입력하시오 > '))
#     for i in range(Num):
#         number = int(input())
#         print(f'출력 = {number}')

# 문제 4

# TC = int(input('TC의 갯수를 입력하시오 > '))

# for tc in range(1, TC + 1):
#     Num = int(input('줄 수를 입력하시오 > '))
#     for _ in range(Num):
#         number = int(input())
#         print(f'{_ + 1} : {number}')

# 문제 5
import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    Num = int(input())
    for i in range(Num):  
        print(input())

# 문제 6

# TC = int(input('TC의 갯수를 입력하시오 > '))

# for tc in range(1, TC + 1):
#     Num = int(input('줄 수를 입력하시오 > '))
#     for i in range(Num):
#         number = list(map(int,input().split()))
#         print(*number)

# 문제 7

# TC , Num = map(int, input('TC, Num의 갯수를 입력하시오 > ').split())

# for tc in range(1, TC + 1):
#     for i in range(Num):
#         number = int(input())
#         print(number)

# 문제 8

# TC , Num = map(int, input('TC, Num의 갯수를 입력하시오 > ').split())

# for tc in range(1, TC + 1):
#     for i in range(Num):
#         number = list(map(int,input().split()))
#         print(*number)

# 문제 9

# TC , Num = map(int, input('TC, Num의 갯수를 입력하시오 > ').split())

# for tc in range(1, TC + 1):
#     for i in range(Num):
#         number = list(map(int,input().split()))
#         print(*number)

