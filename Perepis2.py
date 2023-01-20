a = int(input())
b = int(input())
with open('Perepis.txt', 'r')as f:
    for i in f:
        if a <= int(i[len(i) - 5:-1:]) <= b:
            print(i[:-1])
