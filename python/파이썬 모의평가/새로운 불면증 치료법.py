TC = int(input())
for tc in range(1, TC + 1):
    number = int(input())
    string = []
    calcul = []
    for cnt in range(1, 10**6):
        cal = str(number * cnt)
        for j in range(len(cal)):
            if cal[j] not in string:
                string.append(cal[j])
                calcul.append(int(cal[j]))
                # string.sort()
        if sum(calcul) == sum(range(10)):
            if '0' in string:
                print(f'#{tc} {cal}')
                break