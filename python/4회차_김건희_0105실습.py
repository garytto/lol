import datetime
# 문제 1

# string = input('문자열을 입력하세요 > ')
# cnt = 0
# for element in string:
#     if element == 'e':
#         cnt += 1

# print(cnt)

# 문제 2

# string = input('문자열을 입력하세요 > ')
# cnt = 0
# for str in string:
#     if str == 'a' or str == 'A' or str == 'e' or str == 'E' or str == 'i' or str == 'I' or str == 'o' or str == 'O' or str == 'u' or str == 'U':
#         cnt += 1

# print(cnt)

# 문제 3
# year = datetime.date.today()

# dict_variable = {
#     "이름": "정우영",
#     "생년": "20000101",
#     "회사": "하이퍼그로스",
# }

# birth = int(dict_variable["생년"][0:4])
# age = int(year.year) - birth

# print('나이 : ', age +1, '살')

# 문제 4

# dict_variable = {"name" : "", "phone" : "", "place" : ""}
# dict_variable["name"] = input("이름을 입력하세요 > ")
# dict_variable["phone"] = input("전화번호를 입력하세요 > ")
# dict_variable["place"] = input("거주지를 입력하세요 > ")

# print("이름 : " , dict_variable["name"])
# print("전화번호 : " , dict_variable["phone"])
# print("거주지 : " , dict_variable["place"])

# 문제 5
# dict_variable = {"이름" : "", "인적사항" : {"번호" :" ","이메일" : " ", "거주지" : " "}}
# dict_variable["이름"] = input("이름을 입력하세요 > ")
# dict_variable["인적사항"]["전화번호"] = input("전화번호를 입력하세요 > ")
# dict_variable["인적사항"]["이메일"] = input("email을 입력하세요 > ")
# dict_variable["인적사항"]["거주지"] = input("거주지를 입력하세요 > ")
# print(dict_variable["이름"], dict_variable["인적사항"])


# 문제 6
# yes = str(input("문자열을 입력하세요 > "))
# dict_variable = {}

# for i in yes:
#     if i in dict_variable:
#         dict_variable[i] += 1
#     else:
#         dict_variable[i] = 1

# for key in dict_variable:
#     print(key, dict_variable[key])

