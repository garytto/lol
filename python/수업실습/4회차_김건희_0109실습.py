# 문제1
# string = input()

# for i in range(len(string)):
#     if 'e' in string[i]:
#         print(i)
#     elif 'e' not in string:
#         print('-1')
#         break

# 문제 2

# string = input().split()
# string_list = {}
# for element in string:
#     if element not in string_list: # 잘 기억해야함... 자꾸 햇갈려서 해매면안됨 ㅠㅠ./..
#         string_list[element] = 1 # 해당 문구의 의미는 없다면 생성이라는 의미임
#     elif element in string_list:
#         string_list[element] += 1 # 있다면 숫자 추가

# for key in string_list:
#     print(key, string_list[key]) # 출력


# 문제 3

# string = input('문자열을 입력하세요 > ')
# string_list = list(string)
    
# for i in range(len(string_list)):
#     if 'e' in string_list:
#         string_list.remove('e')    

# save = ''.join(s for s in string_list)        
# # print(string_list)
# print(save)

# 문제 4

# string = input('문자열을 입력하세요 > ').split()
# string_list = list(string[0]) ## 탐색값 용 변환, hello 입력 후 출력 시 h , e , l , l ,o
# cnt = 0
# for i in range(len(string_list)):
#     if string[1] in string_list[i]: # 탐색
#         cnt += 1 # 있따면 1
# print(cnt)

# 문제 5

# number = list(map(str, input(').split()))
# print(*number[0],'-', *number[1], '-', *number[2])

# 테스트

# num1 = int(number[0])
# num2 = int(number[1])
# num3 = int(number[2])
# print(num1,'-', num2, '-', num3) # num1에서 숫자 0이 사라짐 자꾸..


    # 문자열 입력 받았을 때 음수로 입력했는지에 대한 검증을 bool함수를 통해 하려다가 실패..
    # minus가 True 인 경우 양의 정수가 아닙니다 출력 및 종료 하려했으나, 음수가 아니여도 ... 발생...
    # if int(number[i]) > 0:
    #     print(minus)
    #     minus == True
    #     if minus is True:
    #         print('양의 정수가 아닙니다.')
    # elif minus == False:
    #         print(number)
    #         print(minus)

# 문제 6

# number = int(input('양의 정수를 입력하세요 > '))
# num_hundread = int(number/100)
# num_ten = int(number/10) - int(num_hundread*10)
# number_1 = int(number%10)
# sum = num_hundread + num_ten + number_1
# if number < 0:
#     print(-1)
# else:
#     print(sum)


int = int(input())
int += 543
print(int)