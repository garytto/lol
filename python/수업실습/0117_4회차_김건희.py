# 10818 최소,최대
# numberlength = int(input())
# numbers = list(map(int, input().split()))
# numberlist = []
# for i in range(numberlength):
#     numberlist.append(numbers[i])
# numberlist.sort()
# print(f'{numberlist[0]} {numberlist[numberlength-1]}')

# 11720 숫자의 합
# numberlength = int(input())
# numbers = list(map(int, input()))
# numberlist = []
# for i in range(numberlength):
#     numberlist.append(numbers[i])
# print(sum(numberlist))

#2750 수 정렬하기
# numberlength = int(input())
# numbers = []
# for i in range(numberlength):
#     n = int(input())
#     numbers.append(n)
# numbers.sort()
# for i in range(numberlength):
#     print(numbers[i])

# 2562 최대값
numbers = []
for i in range(9):
    numbers.append(int(input()))
mNum = max(numbers)
for i in range(len(numbers)):
    if numbers[i] == mNum:
        print(mNum)
        print(i+1) # i로 출력 시 인덱스 값인 7만 출력됨. 우리가 원하는건 순서임. 그러므로 +!