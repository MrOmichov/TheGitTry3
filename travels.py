L = [0, 0, 0]
smg1 = 0
smg2 = 0
smg3 = 0
with open('travels.txt', 'r') as f:
    for i in f:
        if int(i.split()[0]) == 1:
            smg1 += int(i.split()[6])
            L[0] += 1
        elif int(i.split()[0]) == 2:
            smg2 += int(i.split()[6])
            L[1] += 1
        else:
            smg3 += int(i.split()[6])
            L[2] += 1
    print(L.count(max(L)) + 1)
    print(smg1, smg2, smg3)
smg1 = 0
with open('travels.txt', 'r') as f:
    for i in f:
        if i.split()[2] == 'Липки':
            smg1 += int(i.split()[6])
print(smg1)
smg1 = 0
with open('travels.txt', 'r') as f:
    for i in f:
        if int(i.split()[0]) == 1:
            smg1 += int(i.split()[4])
print(smg1)



