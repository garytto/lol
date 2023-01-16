# 예제 1
# 숫자를 입력 받고, 10을 더해서 출력하세요.
# number1 = int(input("숫자를 입력해주세요 : "))
# print(number1 + 10)

# 예제 2
# 좋아하는 음식을 입력 받고, 출력하세요
# favoritefood = input("좋아하는 음식을 입력해주세요 : ")
# print(favoritefood)

# 예제 3
# 이름과 태어난 년도를 입력 받고, 출력하세요.(단, 태어난 년도를 나이로 변환해서 출력하세요.)
# name = input("이름을 입력해주세요. : ") # 이름 입력
# birth = int(input("태어난 년도를 입력해주세요 : "))# 나이 입력, int로 값 저장
# age = int(2023 - birth) 
# print("저의 이름은 " , name ,"이고, 올해 나이는 " , age ,"세 입니다.")

# 예제 4
# 문장 두 개를 입력 받고, 두 문장을 연결해서 출력하세요.

# first = input("첫 번째 문장을 입력해주세요 : ") # Hello 입력
# second = input("두 번째 문장을 입력해주세요 : ") # world 입력
# print(first + second) # Helloword 출력

# 예제 5
# 숫자 한 개를 입력 받고, 숫자의 부호를 바꿔서 출력하세요. 
# number = input("숫자를 입력하세요 : ") # 10 입력
# number = -int(number) # number의 값을 -int(number)로 변경
# print(number) # -10 출력

# 예제 6
# 숫자 두 개를 입력 받고, 두 숫자에 대한 아래 산술 연산 결과를 출력하세요
# 1. 더하기 , 2. 빼기, 3. 곱하기, 4. 몫, 5. 나머지
# number1 = int(input("첫 번째 숫자를 입력하세요 : ")) # 5 입력
# number2 = int(input("두 번째 숫자를 입력하세요 : ")) # 2 입력

# number3 = int(number1 + number2)
# print("더하기 연산 : " , number3) # 7

# number3 = int(number1 - number2)
# print("빼기 연산 : " , number3) # 3

# number3 = int(number1 * number2)
# print("곱하기 연산 : " , number3) # 10

# number3 = int(number1 / number2)
# print("몫 연산 : " , number3) # 2

# number3 = int(number1 % number2)
# print("나머지 연산 : " , number3) # 1

# 예제 7
# 정수형 숫자 세 개를 입력 받고, 세 정수형 숫자의 평균을 출력하세요.

# number1 = int(input("첫 번째 정수형 숫자를 입력해주세요 > "))
# number2 = int(input("두 번째 정수형 숫자를 입력해주세요 > "))
# number3 = int(input("세 번째 정수형 숫자를 입력해주세요 > "))

# avr = int((number1 + number2 + number3) / 3)
# print("세 정수의 평균은 : ", avr)

# 예제 8
# 정수형 숫자 다섯 개를 입력 받고, 다섯 개의 정수형 숫자를 리스트 객체에 저장해서 출력하세요.
# list_number = [] #입력 받은 정수형 숫자를 저장하는 리스트 객체 생성. number로 명칭
# number1 = int(input("첫 번째 정수형 숫자를 입력해주세요 > "))
# list_number.append(number1)
# number2 = int(input("두 번째 정수형 숫자를 입력해주세요 > "))
# list_number.append(number2)
# number3 = int(input("세 번째 정수형 숫자를 입력해주세요 > "))
# list_number.append(number3)
# number4 = int(input("첫 번째 정수형 숫자를 입력해주세요 > "))
# list_number.append(number4)
# number5 = int(input("두 번째 정수형 숫자를 입력해주세요 > "))
# list_number.append(number5)
# print(list_number)

# 예제 9
# 문자열 하나와 정수형 숫자 한 개를 입력 받고, 문자열을 정수형 숫자만큼 반복해서 출력하세요.
# word = str(input("문자열을 입력해주세요 > ")) # Hello
# number = int(input("정수형 숫자를 입력해주세요 > " )) # 5
# print(word * number)

# 예제 10
# 정수형 숫자 다섯 개를 입력 받고, 입력할 때 마다 입력한 정수형숫자들의 합을 출력하세요.
number = int(input("첫 번째 정수형 숫자를 입력해주세요 > "))
temp = 0
temp += number
print(temp)

number = int(input("두 번째 정수형 숫자를 입력해주세요 > "))
temp += number
print(temp)

number = int(input("세 번째 정수형 숫자를 입력해주세요 > "))
temp += number
print(temp)

number = int(input("네 번째 정수형 숫자를 입력해주세요 > "))
temp += number
print(temp)

number = int(input("다섯 번째 정수형 숫자를 입력해주세요 > "))
temp += number
print(temp)


# 차후 상기 내용은 python에서의 반복문을 알게된다면 짧게 간추릴 수 있을듯.