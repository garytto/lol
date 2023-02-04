# 10101 삼각형 외우기
# angle = [int(input()) for i in range(3)]

# if sum(angle) == 180:
#     if angle[0] == angle[1] == angle[2]:
#         print('Equilateral')
#     elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
#         print('Isosceles')
#     else:
#         print('Scalene')
# else:
#     print("Error")

# 2720 세탁소 사장 동혁
# import sys
# input = sys.stdin.readline

# T = int(input())
# for i in range(T):
#     money = int(input())
#     Quarter = money//25
#     money %= 25
#     Dime = money //10
#     money %= 10
#     Nickel = money //5
#     money %= 5
#     Penny = money
#     print(Quarter, Dime, Nickel, Penny)

# 1453 피시방 알바
# import sys
# input = sys.stdin.readline

# people = int(input())
# people_list = list(map(int,input().split()))

# sit = []
# sum = 0

# for i in range(people):
#     if people_list[i] in sit:
#         sum += 1
#     else:
#         sit.append(people_list[i])
# print(sum)

# 10773 제로
# import sys
# input = sys.stdin.readline

# number = int(input())
# list = []

# for i in range(number):
#     num = int(input())
#     if num == 0:
#         list.pop()
#     else:
#         list.append(num)

# print(sum(list))

#  2161 카드

# import sys
# input = sys.stdin.readline

# N = int(input())
# card_list = [i for i in range(1, N+1)]
# discarded_card = []

# while len(card_list) != 1:
#     discarded_card.append(card_list.pop(0)) #버리기
#     card_list.append(card_list.pop(0)) #뒤로 옮기기

# for i in discarded_card:
#     print(i, end = ' ')
# print(card_list[0])

# 9012 

# import sys
# input = sys.stdin.readline

# T = int(input())
# for i in range(T) :
#     array = list(input())
#     answer = 0
#     for j in array :
#         if j == "(" :
#             answer += 1
#         elif j == ")" :
#             answer -= 1
#         if answer < 0 :
#             print('NO')
#             break

#     if answer == 0 :
#         print('YES')
#     elif answer > 0 :
#         print('NO')    
