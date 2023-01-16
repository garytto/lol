# 예제 1
# number1 = 1
# number2 = number1 + 1
# print(number1, number2) # 1 2
# 주석 만들기 : 앞에 #을 넣던가, ctrl + /



# 예제 2
# number1 = 10
# number2 = 5
# number3 = str(number1) + str(number2)
# number4 = number1 + number2
# print(number1, number2, number3, number4) # 10, 5 , 문자열상태(105), 15



# 예제 3
# string1 = "Hello"
# string2 = string1
# string3 = "Wolrd" + "!"
# print(string2, "?", string3) # Hello ? World!


# 예제 4
# string = "Hello?"
# n = 5
# print(string * n) # Hello?Hello?Hello?Hello?Hello?



# 예제 5
# string = "abc hello def"
# sub_string1 = string[4:10]
# sub_string2 = string[1:4]
# sub_string3 = string[-1]

# print(sub_string1) # hello
# print(sub_string2) # bc h
# print(sub_string3) # f 
# ## 예제 5 추가 테스트
# sub_string4 = string[-8:-1]
# print(sub_string4) # ello de

# 예제 6
# number1 = 5
# number2 = 10.0 + number1
# number1 - 5 #내부 값 변경을 원한다면 -가 아닌 -= 를 통해 진행하여야함.
# number3 = number1 * (number2 + 10)

# print(number1, number2, number3) # 5 , 15.0, 100

# 예제 7
# list_variable = [1, 2, 3, [1,2,3]]
# sub_list = list_variable[3][-1]

# print(sub_list) # 3 // [3] <- 4번째 순서의 [-1] < - 뒤에서 첫 번째

#예제 8
# list_variable = []
# list_variable.append(1) #list에 1 추가
# list_variable.append("a") #list에 "a" 추가
# list_variable[0] = 0 #list 첫번째 값은 0이다라고 재 정의

# print(list_variable) # 0, "a"

#예제 9
# name = input("너의 이름은?") # name에 들어갈 값을 입력하시오

# print(name) # input기능을 통해 입력된 name 값 출력.

#예제 10

age = int(input("너의 나이는?")) # input기능을 통해 입력한 값을 int(정수)화 시켜 age에 저장

print("올해 나이 : ", age) # 올해 나이 : (age 값)
print("내년 나이 : ", age + 1) # 올해 나이 : (age 값 + 1)