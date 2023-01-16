# 예제 1

# dict_variable = {}
# dict_variable["이름"] = "정우영"
# dict_variable["생년월일"] = "19000101"
# dict_variable["회사"] = "하이퍼그로스"

# print(dict_variable["이름"]) # 정우영
# print(dict_variable["생년월일"]) # 1900101
# print(dict_variable["회사"]) # 하이퍼그로스

# 예제 2

# dict_variable = {"a": "A", "B": "b"}
# dict_variable["c"] = "C"
# dict_variable["D"] = "d"
# dict_variable["e"] = "E"


# print(dict_variable["a"]) # A
# print(dict_variable["D"]) # d 
# print(dict_variable["b"]) # 오류 발생. 키 값이 아닌 내부 값으로 읽어오려했기 때문. b가 아닌 B였으면 문제 없이 작동했을 것.

# 예제 3

# dict_variable = {}
# dict_variable["apple"] = 5000
# dict_variable["banana"] = 3000
# dict_variable["apple"] = 2000
# dict_variable["banana"] = dict_variable["banana"] + 1000

# print(dict_variable["apple"] + dict_variable["banana"]) # 6000 apple은 3번째 코드로 인해 2000원으로 재 정의, banana의 경우 기존 값에서 1000원 추가로 재 정의

# 예제 4

# dict_variable = {
#     "이름": "정우영",
#     "생년월일": "19000101",
#     "회사": "하이퍼그로스",
# }

# for key in dict_variable:
#     print(key, dict_variable[key]) # 키 값과 연겯뢰어있는 내부 값 출력하라는 함수임... 키값만 노출이 되는것이 아님. 잘 기억하자..

"""
예측을 작성하세요.
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""

# 예제 5

# dict_variable = {
#     "이름": "정우영",
#     "생년월일": "19000101",
#     "회사": "하이퍼그로스",
# }

# for key, value in dict_variable.items(): # items가 들어간 이유. 앞에 key, value를 동시에 돌리기 위해.
#     print(key, value) 

"""
예측을 작성하세요.
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""

# 예제 6

# dict_variable = {
#     "이름": "정우영",
#     "생년월일": "19000101",
#     "회사": "하이퍼그로스",
# }

# print("나이" in dict_variable) # False dict_variable에는 나이라는 키값이 없기에. False가 나온다. 만약 키와 연동된 내부 값인 "정우영"등을 기입해도 해당 내용은 키 값이 아닌 내부 값이므로 False가 출력된다.

# 예제 7

# dict_variable = {
#     "이름": "정우영",
#     "생년월일": "19000101",
#     "회사": "하이퍼그로스",
# }

# if "거주지" not in dict_variable:
#     dict_variable["거주지"] = "서울특별시"
#     # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
#     # dict_variable이라는 딕셔너리에 "거주지" 키값이 없다면, "거주지" 키값과 해당 키에 맵핑되어있는 "서울특별시"를 추가한다.
    
# print(dict_variable) # {'이름' : '정우영', '생년월일': '19000101'. '회사': '하이퍼그로스', '거주지': '서울특별시'}

# 예제 8

# list_variable = []

# try:
#     list_variable.append(0)
#     list_variable.append(1)
#     list_variable.append(2)
#     print(list_variable[3])
    
# except:
#     print("에러가 발생했습니다.")
#     print("에러의 원인은 무엇인가요?")

"""
출력 결과를 예측해서 작성하세요.
에러가 발생했습니다.
에러의 원인은 무엇인가요?  list_variable 이라는 리스트에는 0,1,2의 값만 있지만(인덱스 0, 인덱스 1, 인덱스 2), print 함수에서는 list_variable 리스트에는 없는 인덱스 3의 값을 요구하고 있음,
"""

# 예제 9

# try:
#     number = 1
#     if number == 1
#         print(number)
    
    
# except:
#     print("에러가 발생했습니다.")
#     print("에러의 원인은 무엇인가요?")

"""
에러 원인
if number == 1: <- if문에 :요거 빠져있어요.
""" 

# 예제 10

n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0: # 짝수 
        total += number * 2 # 60
    elif number % 2 == 1: #홀수
        total += number + 1 * 3 # 40 , 25 + 15

print(total) # 100


