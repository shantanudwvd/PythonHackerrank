def angryProfessor(k, a):
   count = 0
   i = 0
   while i < len(a):
       if a[i] <= 0:
           count += 1
       i += 1
   if count >= k:
       return 'NO'
   else:
       return 'YES'


t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    result = angryProfessor(k, a)
print(result)
