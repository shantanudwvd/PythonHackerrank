def average(array):
    my_set = ()
    my_set = array
    my_set = set(my_set)
    avg=sum(my_set)/len(my_set)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

