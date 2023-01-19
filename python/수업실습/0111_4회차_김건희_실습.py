# 문제 1
# string = input()
# print(string.upper())

# 문제 2 - 1

# number = int(input())
# numbers = []
# for i in range(number+1): # 숫자 넣기
#     numbers.append(i)

# numberssum = sum(numbers) # 숫자 합계 구하기
# print(numberssum)

# 문제 2 - 2
# number = int(input())
# numbersum = int(0)
# for i in range(number+1): # 숫자 계산
#     numbersum += i
# print(numbersum)

# 문제 3
# a , b = map(int, input().split())
# game = True

# while game:
#     if a == 1 and b == 3:
#         print('A')
#         break
#     elif b == 1 and a == 3:
#         print('B')
#         break
#     elif a < b:
#         print('B')
#         break
#     elif b < a:
#         print('A')
#         break

# 문제 4

# a = '+'
# b = '#'
# for i in range(4):
#     print(f'{a*i}{b}{a*(4-i)}')

# 문제 5

# Number = input() # 문자열로 값 받고(for문 안돌리는 이유 범위가 지정되있긴 하나 귀찮아서.)
# print(type(Number)) # 혹시몰라서 str값이 맞는지 확인용.
# result = 0 # 총합 저장용
# for i in range(len(Number)): #반복용
#     result += int(Number[i]) #문자열 각각 정수로 치환하여 저장용에 추가 /if = input : 820394,이건 '8'+'2'+'0'+'3'+'9'+'4' 랑 같은 의미
#     print(result) # 정상적으로 계산되는지 확인용
# print(result) # 결과 출력

# 문제 6

number = int(input())

numberlist = []

for i in range(number+1):
    cal = 1 * (2**i)
    numberlist.append(cal)

print(*numberlist)