# 문제 1 10개의 수를 입력 받아, 그 중에 홀수만 더하는것
TC = int(input())

for tc in range(1, TC + 1):
    number = list(map(int,input().split()))
    result = 0
    for i in range(len(number)):
        if number[i]%2 > 0:
            result += number[i]
    print(f'#{tc} {result}')