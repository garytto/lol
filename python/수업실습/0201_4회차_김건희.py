import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

# # 2525 오븐 시계

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

# 2798 블랙잭 
# def 안 쓴 풀이
# N , M = map(int,input().split())
# numbers = list(map(int,input().split()))
# n_sum = 0

# for i in range(N-2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             tmp = numbers[i] + numbers[j] + numbers[k]
            
#             if n_sum < tmp <= M:
#                 n_sum = tmp
            
#             if n_sum == M:
#                 break
# print(n_sum)

# def 사용 풀이 return을 사용하여 모든 과정을 스킵하고 바로 결과를 도출하는 면 때문인지 def 안쓴 풀이에 비해 속도가 더 빠름.
# N , M = map(int,input().split())
# numbers = list(map(int,input().split()))
# def result(n, m, number):
#     n_sum = 0

#     for i in range(n-2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 tmp = number[i] + number[j] + number[k]
#                 if n_sum < tmp <= m:
#                     n_sum = tmp
#                 if n_sum == m:
#                     return tmp

#     return n_sum
# print(result(N, M, numbers))

# 9076 점수 집계
# TC = int(input())
# for i in range(TC):
#     number_list = list(map(int, input().split()))
#     number_sort = sorted(number_list)
#     number_sort.pop(0)
#     number_sort.pop(3)
#     num_gap = number_sort[2] - number_sort[0]

#     if num_gap >= 4:
#         print('KIN')
#     else:
#         print(sum(number_sort))



# 1526 다른 풀이

# N=int(input())
# ans=0

# def find(i) :
#     for s in str(i) :
#         if s not in ['4', '7'] :
#             return False
#     return True

# for i in range(4, N+1) :
#     if find(i) :
#         ans=int(i)

# print(ans)




# 1526 가장 큰 금민수
# number = int(input())

# while True:
#     if len(str(number)) == str(number).count('4') + str(number).count('7'): # 4또는 7이 도합해서 number의 자릿수 까지만 있기 때문에 접근
#         print(number)
#         break
#     number -= 1




# 1436 영화감독 숌
number = int(input())
cnt = 0
num = 0
# 666 <
while True:
    if "666" in str(num): # 숫자에 666이 포함되는 순간 카운트 + 1 요 if 문을 뒤에 넣었더니 break가 우선되어 제대로 된 값이 나오지 않음.
        cnt += 1
    
    if cnt == number: # 
        print(num)
        break

    num += 1 # 다음번 666이 나올때까지 계에에에에속 더하기
