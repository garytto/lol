# num = int(input("숫자를 입력하세요 > "))

# if num <= 0:
#     print("0보다 큰 양의 정수를 입력하세요.")
# else:
#     if num%2 == 1:
#         print("홀수")
#     else:
#         print("짝수")

# dust = int(input("미세먼지 농도를 입력하세요 > "))

# if dust < 0:
#     print('0보다 낮은 수치는 존재할 수 없습니다. 다시 입력하세요')
# elif dust <= 30:
#     print('좋음')
# elif dust < 80:
#     print('보통')
# elif dust < 151:
#     print('나쁨')
# elif dust > 150:
#     print('매우나쁨')
# elif dust > 300:
#     print('실외 활동을 자제하세요.')

# a = 'pineapple'

# for i in range(len(a)):
#     print(a[i])


# word = 'apple'

# # a가 있으면, 1을 출력
# if 'a' in word:
#     print('1')

# # a가 있을때마다, 1을 출력 인경우에는.
# for char in word:
#     # print(char) # 겸사 겸사 확인.
#     if char == 'a':
#         print('1')


# word = 'mango'

# # 'e'가 있으면 1을 출력
# # 'e'가 없으면 0을 출력
# in_end = False

# for char in word:
#     if char == 'e':
#         print(1)
#         is_end = True
#         break

a = int(input())
b = int(input())

print(a+b)