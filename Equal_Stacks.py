s1, s2, s3 = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
sum1 = sum(a1)
sum2 = sum(a2)
sum3 = sum(a3)
i1 = 0
i2 = 0
i3 = 0
while True:
    if sum1 == sum2 and sum2 == sum3:
        print(sum1)
        break
    elif sum1 == 0 or sum2 == 0 or sum3 == 0:
        print("0")
        break
    elif sum1 > sum3 and sum2 > sum3:
        sum1 -= a1[i1]
        i1 += 1
        sum2 -= a2[i2]
        i2 += 1
    elif sum2 > sum1 and sum3 > sum1:
        sum2 -= a2[i2]
        i2 += 1
        sum3 -= a3[i3]
        i3 += 1
    elif sum1 > sum2 and sum3 > sum2:
        sum3 -= a3[i3]
        i3 += 1
        sum1 -= a1[i1]
        i1 += 1
    elif sum1 > sum2 and sum1 > sum3:
        sum1 -= a1[i1]
        i1 += 1
    elif sum2 > sum1 and sum2 > sum3:
        sum2 -= a2[i2]
        i2 += 1
    elif sum3 > sum1 and sum3 > sum2:
        sum3 -= a3[i3]
        i3 += 1
    else:
        sum1 -= a1[i1]
        i1 += 1
        sum2 -= a2[i2]
        i2 += 1
        sum3 -= a3[i3]
        i3 += 1
