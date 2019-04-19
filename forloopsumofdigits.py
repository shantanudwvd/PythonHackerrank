n = int(input())
sum_of_digits = 0
for i in range(n):
    if n == 0:
        break
    else:
        sum_of_digits += n % 10
        n = n/10
        n = int(n)
print(sum_of_digits)
