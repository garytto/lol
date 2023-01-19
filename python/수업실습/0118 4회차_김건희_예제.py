import sys
input = sys.stdin.readline

# 2789 유학금지

# string = input().rstrip()
# for i in 'CAMBRIDGE':
#     if i in string:
#         string = string.replace(i, "")
# print(string)

# 문자열 반복
# TC = int(input())

# for tc in range(TC): # 편의를 위해 0부터 시작하는게 아닌 1로 시작. 첫번째 두번째 세번째.... 로 생각하기 편하게 하기 위해
#     num, string = input().rstrip().split()
#     result = ''
#     int(num)
#     for i in string:
#         result += i*num
#     print(result)

# 10988 펠린드롬
# string = input().rstrip()
# if string == string[::-1]:
#     print('1')
# else:
#     print('0')

# 17249 태보 태보 총 난타
# a, b = input().rstrip().split('(^0^)') # 얼굴을 기점으로 하여 a, b 를 나누어 저장(왼 오른)
# A = a.count('@') # 주먹의 잔상을 구하는 문제이기에 주먹의 갯수만 세기
# B = b.count('@')
# print(A, B)

# 2941 크로아티아 알파벳
# string = input().rstrip()
# sList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for i in sList:
#     string = string.replace(i, "@") # 변환하여 임의의 한글자로 변경.
# print(len(string))
    
# 10809 알파벳 찾기
string = input().rstrip()
Alphabat = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v','w','x','y','z']
for i in Alphabat:
    if i in string:
        print(string.index(i),end = " ")
    else:
        print('-1', end = " ")