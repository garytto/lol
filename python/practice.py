# 문제 1

# a = str(input('문자열을 입력하세요 > '))

# cnt = 0
# for name in a:
#     if name == 'e':
#         cnt += 1

# print(cnt)

# 문제 2

# a = str(input('문자열을 입력하시오 > '))

# moeum_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
# cnt = 0
# h = len(moeum_list)
# print(h)
# for num in a:
#     for i in range(h):
#         if num == moeum_list[i]:
#             cnt += 1
# print(cnt)

# 문제 3
# import datetime

# dict_variable = {
#     "이름" : "김건희",
#     "생년" : "19960912",
#     "회사" : "하이퍼그로스"
# }

# year = datetime.date.today()
# birth = dict_variable["생년"][0:4]
# age = int(year.year) - int(birth)
# print(age)

# 문제 4

# info = {}
# info['이름'] = str(input('이름을 입력하시오 > '))
# info['전화번호'] = str(input('전화번호를 입력 하시오 > '))
# info['거주지'] = str(input('거주지를 입력 하시오 > '))

# for a in info:
#     print(a,':', info[a])

# 문제 5

info = {}
info['이름'] = str(input('이름을 입력하시오 > '))
info['인적사항'] = {}
info['인적사항']['전화번호'] = str(input('전화번호를 입력하시오 > '))
info['인적사항']['이메일'] = str(input('이메일을 입력 하시오 > '))
info['인적사항']['거주지'] = str(input('거주지를 입력 하시오 > '))

print(info.values())