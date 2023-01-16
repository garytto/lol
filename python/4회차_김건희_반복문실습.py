# 문제 1
# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.

# num = int(input("정수를 입력하세요 > "))
# if num > 0:
#     print(True)
# elif num == 0:
#     print("그것은 0 입니다.")
# else:
#     print(False)
    

# 문제 2
# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요

# num1 = int(input("첫 번째 정수를 입력하세요. > "))
# num2 = int(input("두 번째 정수를 입력하세요. > "))
# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# else:
#     print("두 개의 정수를 다시 입력하세요. 두 값이 동일합니다.")

# 문제 3
# 정수 한 개를 입력 받고, 해당 정수가 1보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.

# 버전 1
#num = int(input("정수를 입력하세요 > "))
# if num > 1:
#     if num < 10:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

# 버전 2
# num = int(input("정수를 입력하세요 > "))
# if num > 1 and num < 10:
#     print(True)
# else:
#     print(False)

# 문제 4
# 정수 한 개를 입력 받고 0보다 크고, 짝수라면 True 아니면 False를 출력하세요.
# num = int(input("정수를 입력하세요 > "))

# if num > 0 and num%2 == 0:
#     print(True)
# else:
#     print(False)


# 문제 5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

# num = int(input("정수를 입력하세요 > "))

# if num <= 100 and num > 0:
#     if num >= int(60):
#         print("합격")
#     else:
#         print("불합격")
# else:
#     print("ERROR")

# 문제 6
# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.

# word = input("문자열을 입력하세요 > ")
# word = word[::-1] # 반전
# print(word)
# for element in word:
#     print(element) # 한 글자씩 출력

# 문제 7
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같다면 False를 출력.

# num1 = int(input("첫 번째 정수를 입력하세요 > "))
# num2 = int(input("두 번째 정수를 입력하세요 > "))

# if num1 > num2:
#     for element in range(num2, num1+1):
#         print(element)
# elif num1 < num2:
#     for element in range(num1, num2+1):
#         print(element)
# elif num1 == num2:
#     print(False)

# 문제 8
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.
# 두 값이 같으면 False를 출력하세요.

# num1 = int(input("첫 번째 정수를 입력하세요 > "))
# num2 = int(input("두 번째 정수를 입력하세요 > "))

# if num1 > num2:
#     list = range(num2, num1+1)
#     list = list[::-1]
#     for element in list:
#         print(element, end = " ")
# elif num1 < num2:
#     list = range(num1, num2+1)
#     list = list[::-1]
#     for element in list:
#         print(element, end = " ")
# elif num1 == num2:
#     print(False)

# 문제 9
# 정수 한 개를 입력 받고, 1부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

# num = int(input("정수를 입력하세요 > "))

# if num > 1:
#     list = range(1, num, 2)
#     for element in list:
#         print(element)
# elif num <= 1:
#     print(False)

# 문제 10
# 구구단을 출력하세요.

# for i in range(1, 10):
#     for j in range (1, 10):
#         print(i,'x',j,'=', i*j) 