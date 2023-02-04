import sys
# input = sys.stdin.readline

# 2441 별찍기
# n = int(input())

# for i in range(n):
#     print(" " * i + "*"*(n - i))

# 2592 대표값

# numbers = []
# cnt = 0
# result = 0

# for i in range(10):
#     numbers.append(int(input()))

# for i in range(10): 
#     if cnt < numbers.count(numbers[i]):
#         cnt = numbers.count(numbers[i])
#         result = numbers[i]

# print(sum(numbers)//10)
# print(result)

# 2592 2번쨰 풀이
# numbers = [int(input()) for i in range(10)]
# print(sum(numbers)//10)
# print(max(numbers, key = numbers.count))

# 10798
# string = []
# str_len = []
# for i in range(5):
#     a = input()
#     string.append(a)
#     str_len.append(len[a])

# for j in range(max[str_len]):
#     for k in range(5):
#         try:
#             print(string[k][j], end = "")
#         except:
#             continue

# 9455

# 1652
# 가로 세로 한줄씩 확인하여 눕기가 가능한지 확인하는 문제.
sys.stdin = open("input.txt", "r")

numbers = int(input())
array = [input()+'X' for _ in range(numbers)] + ['X' *(numbers+1)] #else 대응 용 벽 새우기. 

def check_r():
    result = 0
    for i in range(numbers):
        cnt = 0
        for j in range(numbers+1):
            if array[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
    return result

def check_col():
    result = 0
    for j in range(numbers):
        cnt = 0
        for i in range(numbers+1):
            if array[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
    return result
    
print(check_r(), check_col())
