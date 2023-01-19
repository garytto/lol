# 문제 1
# test_case = int(input())

# for i in range(1, test_case + 1):
#     a, b = list(map(int,input().split()))
#     print(f'#{i} {a//b} {a%b}')


# 문제 2 math 함수 추가 버전 - 수정 진행 예정
# import math
# test_case = int(input())

# for i in range(1, test_case + 1):
#     numbers = list(map(int,input().split()))
#     numbersum = int(sum(numbers))
#     average = numbersum/int(len(numbers)) ## 평균 구하기
#     print(average)
#     average = math.ceil(average) ## 소수점 반올림
#     print(f'#{i} {average}')

# 문제 2 math 함수 없는 버전
# test_case = int(input())

# for i in range(1, test_case + 1):
#     numbers = list(map(int, input().split()))
#     numbersum = int(sum(numbers)) # 차마 합계까지 for 문돌리기 귀찮아서..
#     avg = numbersum//int(len(numbers)) # 평균 구하기

#     numberleft = numbersum % int(len(numbers)) # 나머지 값 여부 확인용
   
#     if numberleft > 0: # 나머지 값이 있다면
#         countleft = int((numberleft/len(numbers)) * 10) # 계산하기 편하기 위해 소숫점 1자리 값만 올리기
#         print(countleft) # 소수점 1자리 에있는 값 출력
#         if countleft > 5: # 소숫 점 1자리에 있는 값이 5보다 높다면... 추가한다 의 계산식 만든것
#             print(avg) # 소숫 점 올리기 전 평균 값
#             avg += 1
#             print(avg)
#     print(f'#{i} {avg}')

# 문제 3
# a, b = list(map(int,input().split()))
# 방법 1
# cal = []
# numbersum = int(a + b)
# numberminus = int(a - b)
# numbermulti = int(a * b) # 곱하기는 영어로 multiplication
# numberdivision = int(a // b) # 나누기는 영어로 division
# cal.append(numbersum)
# cal.append(numberminus)
# cal.append(numbermulti)
# cal.append(numberdivision)
# for i in range(len(cal)):
#     print(f'{cal[i]}')

# 방법 2
# cal2 = [a + b, a - b, a * b, a // b]

# for i in range(len(cal2)):
#     print(f'{cal2[i]}')

# 방법 3

# for i in [a + b, a - b, a * b, a // b]:
#     print(f'{i}')

# 문제 4

# cnt = int(input())
# string = '#'
# string = string * cnt
# print(f'{string}')

# 문제 5

# test_case = int(input())

# for i in range(1, test_case + 1):
#     numbers = list(map(int,input().split()))
#     numbers.sort()
#     print(f'#{i} {numbers[len(numbers)-1]}')

