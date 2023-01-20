s = 0
with open('Perepis.txt', 'r')as f:
    for i in f:
        if int(i[len(i) - 5:-1:]) < 1978:
            s += 1
            print(i[:len(i) - 13:])
    print(s)


