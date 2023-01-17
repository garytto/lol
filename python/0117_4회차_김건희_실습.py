# 9085 더하기
TC = int(input())

for tc in range(1, TC+1):
    numlength = int(input()) # 5 개 더할거다.
    numbers = list(map(int,input().split())) # 숫자를 뭐 6개를 입력을 해도
    numbersum = 0
    
    for i in range(numlength): # 5개만 더할수있게 
        numbersum += numbers[i]

    print(numbersum)

# 10824 네 수
# a, b, c, d = map(int, input().split())
# result = int((str(a) + str(b)))+int(str(c) + str(d))
# print(result)

# 3009 네 번째 점
# a_1, a_2 = map(int,input().split())
# b_1, b_2 = map(int,input().split())
# c_1, c_2 = map(int,input().split())

# def define(a, b, c):
#     if a == b:
#         return c
#     elif b == c:
#         return a
#     elif a == c:
#         return b

# d_1 = define(a_1, b_1, c_1)
# d_2 = define(a_2, b_2, c_2)
# print(d_1, d_2)

# 10952 a + b
# while True:
#     a, b = map(int,input().split())
#     if a != 0 and b != 0:
#         print(a + b)
#     if a == 0 and b == 0:
#         break

# 1110 더하기 사이클
number = int(input())
num = number # 비교용과 나누기 위해
cnt = 0
while True:
    a = num //10 # 10자리
    b = num % 10 # 1자리
    c = (a + b) % 10
    num = (b * 10) + c
    cnt += 1
    if num == number:
        break
print(cnt)


