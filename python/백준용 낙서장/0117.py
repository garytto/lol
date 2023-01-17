# 15552 빠른 A + B
# import sys
# # input = sys.stdin.readline Case 2 
# # input 자체를 sys.stdin.readline으로 변경 함으로써 밑에서 input을 사용해도 문제 없이 readline의 기능을 사용할 수 있음.

# T = int(input())
    
# for i in range(T):
#     a,b = map(int,sys.stdin.readline.split()) # Case 1 용
#     # a,b = map(int,input().split()) Case 2 진행 시 사용
#     print(a+b)

# 2438 별 찍기 - 1
# import sys

# input = sys.stdin.readline
# N = int(input())

# for i in range(1, N+1):
#     print('*'*i)

# 2439 별 찍기 - 2
# import sys
# input = sys.stdin.readline

# N = int(input())
# for i in range(1, N+1):
#     print(' '*(N-i)+('*'*i)) # 초기에 +가아닌 ,로 해서 출력 오류가 남..

# 10951 A + B -4
# import sys
# input = sys.stdin.readline
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         # print('Error')
#         break
# # 시도(Try)할 떄만 작동하는 코드 만들기 예시, Try에 명시되어있는 형태로 진행 안하는경우, except<- 예외처리 진행. 

# 10807 개수 세기
import sys
input = sys.stdin.readline

N = int(input())
Numbers = list(map(int,input().split()))
FNumber = int(input())
cnt = 0
for i in range(len(Numbers)):
    if Numbers[i] == FNumber:
        cnt += 1
print(cnt)