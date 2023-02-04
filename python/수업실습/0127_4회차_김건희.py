import sys
input = sys.stdin.readline

# 10817 세수
# import sys
# input = sys.stdin.readline

# a, b, c = map(int, input().split())
# print(a + b + c - max(a, b, c) - min(a, b, c))

# 20001 고무오리
# cnt=0
# while 1:
#     text = input().rstrip()
#     if text=="고무오리 디버깅 끝":
#         break
#     if text=="문제":
#         cnt+=1
#     elif text=="고무오리" and cnt==0:
#         cnt+=2
#     elif text=="고무오리":
#         cnt-=1
# if cnt > 0:
#     print("힝구")
# else:
#     print("고무오리야 사랑해")

# 1269 대칭 차 집합

# A, B = map(int, input().split())

# a = set(map(int, input().split()))
# b = set(map(int, input().split()))

# print(len(a-b)+len(b-a))

# 3052 나머지

# a = []
# for i in range(10):
#     array = int(input())
#     b = array % 42
#     a.append(b)
# c = set(a)
# print(len(c))

# 1181 단어 정렬
 # 아오오오오 오타 떄문에 삽을 너무 팠따...
# n = int(input())
# ls = []

# for i in range(n):
#     ls.append(input().rstrip())

# s = set(ls)
# ls = list(s)

# ls.sort()
# ls.sort(key=len)

# for i in ls:
#     print(i)

# 11286 절댓값 힙

# import heapq

# N = int(input())
# heap = []

# for _ in range(N):
#     n = int(input())
#     if n != 0:
#         heapq.heappush(heap, (abs(n), n))
    
#     else:
#         if len(heap) != 0:
#             print(heapq.heappop(heap)[1])
#         else:
#             print(0)
