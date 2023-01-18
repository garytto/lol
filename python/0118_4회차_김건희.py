import sys
input = sys.stdin.readline
# 9498 시험성적
a = int(input())

if a <= 100 and a > 89:
    print('A')
elif a > 79: ## elif > 사용 해보기. #
    print('B')
elif a > 69:
    print('C')
elif a > 59:
    print('D')
else:
    print('F')

# 9093 단어 뒤집기
# T = int(input())
# for t in range(1, T+1):
#     string = input().rstrip().split()
#     for i in range(len(string)):
#         string[i] = string[i][::-1]
#     print(*string, end = " ")


# 11721 열 개씩 끊어 출력하기
# string = input().rstrip()
# for i in range(0, len(string), 10): # 어짜피 10 단위로 출력이므로 범위는 0부터 string의 길이만큼 이지만, i의 값은 10씩 추가해서 만 받음.
#     endline = i + 10 # 10개씩 끊어서 출력하니 해당 부분에 대응
#     # print(i) # 정상적으로 순서에 맞춰 진행되는지 확인. 위에 range(0, len(string), 10) <- i가 10씩 되는지 확인용
#     print(string[i:endline])

# 2947 나무조각
numbers = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print(" ".join(map(str, numbers))) # 이 문제는 정답을 찾는 과정을 출력을 같이 해줘야하는 문제이기에..

    if numbers == answer:
        break