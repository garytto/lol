import sys
input = sys.stdin.readline

# 1547 공
# balls = [0, 1, 0, 0]

# for _ in range(int(input())):
#     X, Y = map(int, input().split())
#     temp =  balls[X]
#     balls[X] = balls[Y]
#     balls[Y] = temp
    
# print(balls.index(1))

# 5576 콘테스트

# w = []
# k = []
# =======================
# score_list = []
# for i in range(20):
#     score_list.append(int(input))
# for i in range(0, 10):
#     w.append(score_list[i])
# for i in range(11, 20):
#     k.append(score_list[i])
# ==========================

# for i in range(20):
#     if i < 10:
#         w.append(int(input()))
#     else:
#         k.append(int(input()))
# w = sorted(w, reverse=True)
# k = sorted(k, reverse=True)
# w_ans = w[0] + w[1] + w[2]
# k_ans = k[0] + k[1] + k[2]
# print(w_ans, k_ans)

# 2846 오르막길
# n = int(input())
# numbers = list(map(int, input().split()))

# # result = [] # 아래식이 더 좋으므로 폐기
# # for _ in range(n):
# #     result.append(0) 

# result = [0]*n
# # print(result)
# for i in range(n):
#     cnt = 0
#     for j in range(i+1, n):
#         if numbers[j] > numbers[j-1]:
#             tmp = numbers[j] - numbers[j-1]
#             cnt += tmp
#         else:
#             break
#     result[i] = cnt
# print(max(result))


# 1251 단어 나누기

s = input().rstrip()
answer_list = []
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            answer = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1] # -1로 뒤집고 합친다.
            print(*answer)
            answer_list.append(answer)
answer_list = sorted(answer_list)
print(answer_list[0])
