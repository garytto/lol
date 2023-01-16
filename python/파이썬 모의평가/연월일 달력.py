TC = int(input())
for tc in range(1, TC + 1):
    cal = input()
    year = cal[0]+cal[1]+cal[2]+cal[3]
    month = cal[4] + cal[5]
    day = cal[6] + cal[7]

    num = [1,3,5,7,8,10,11]
    num2 = [4,6,9,11]
    pas = True

    if int(month) > 12 or int(month) <= 0 or int(day) == 0:
        print(f'#{tc} -1')
    else:
        if int(month) == 2:
            if int(day) > 28:
                pas = False
        if int(month) in num:
            if int(day) > 31:
                pas = False
        if int(month) in num2:
            if int(day) > 30:
                pas = False
        if pas == True:
            print(f'#{tc} {year}/{month}/{day}')
        if pas == False:
            print(f'#{tc} -1')