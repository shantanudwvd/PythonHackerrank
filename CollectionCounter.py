import collections
size = int(input())
my_list = list(map(int, input().split()))
my_dict = collections.Counter(my_list)
queries = int(input())
total_cost = 0
for i in range(queries):
    shoe_size, price = input().split()
    shoe_size = int(shoe_size)
    price = int(price)
    for k, v in my_dict.items():
        if shoe_size == k and v > 0:
            my_dict[k] -= 1
            total_cost += price
            break
print(total_cost)
