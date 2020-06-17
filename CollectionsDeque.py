from collections import deque
deq = deque()
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
queries = int(input())
for i in range(queries):
    my_string = input()
    string = ""
    number = ""
    for j in my_string:
        if j not in digits:
            string += j
        else:
            number += j
    if number != "":
        number = int(number)
    if string == "append":
        deq.append(number)
    elif string == "appendleft":
        deq.appendleft(number)
    elif string == "pop":
        deq.pop()
    elif string == "popleft":
        deq.popleft()
for i in deq:
    print(i, end=" ")
