with open('mat_dv.txt', 'r') as f:
    _8 = ['', '', 8, 0]
    _9 = ['', '', 9, 0]
    _10 = ['', '', 10, 0]
    _11 = ['', '', 11, 0]
    for i in f:
        a = i.split()
        a[2] = int(a[2])
        a[3] = int(a[3])
        a[4] = int(a[4])
        if a[3] + a[4] >= _8[3] and a[2] == _8[2]:
            if int(i.split[3]) + int(i.split[4]) == _8[3]:
                _8.extend([a[0], a[1], at[3] + a[4]])
            else:
                _8[0] = a[0]
                _8[1] = a[1]
                _8[2] = a[2]
                _8[3] = a[3] + a[4]
        elif a[3] + a[4] >= _9[3] and a[2] == _9[2]:
            if a[3] + a[4] == _9[3]:
                _9.extend([a[0], a[1], at[3] + a[4]])
            else:
                _9[0] = a[0]
                _9[1] = a[1]
                _9[2] = a[2]
                _9[3] = a[3] + a[4]
        elif int(i.split[3]) + int(i.split[4]) >= _10[3] and i.split[2] == _10[2]:
            if int(i.split[3]) + int(i.split[4]) == _10[3]:
                _10.extend([a[0], a[1], at[3] + a[4]])
            else:
                _10[0] = a[0]
                _10[1] = a[1]
                _10[2] = a[2]
                _10[3] = a[3] + a[4]
        elif a[3] + a[4] >= _11[3] and a[2] == _11[2]:
            if a[3] + int(i.split[4]) == _11[3]:
                _11.extend([a[0], a[1], at[3] + a[4]])
            else:
                _11[0] = a[0]
                _11[1] = a[1]
                _11[2] = a[2]
                _11[3] = a[3] + a[4]
    print(_8)


with open('mat_dv.txt', 'r') as f:
    algebra = ['', '', 0, 0]
    geometry = ['', '', 0, 0]
    for i in f:
        if int(i.split()[3]) >= algebra[3]:
            if int(i.split()[3]) == algebra[3]:
                algebra.extend([i.split()[0], i.split()[1], int(i.split()[2]), int(i.split()[3])])
            else:
                algebra[0] = i.split()[0]
                algebra[1] = i.split()[1]
                algebra[2] = int(i.split()[2])
                algebra[3] = int(i.split()[3])
        if int(i.split()[4]) >= geometry[3]:
            if int(i.split()[3]) == geometry[3]:
                geometry.extend([i.split()[0], i.split()[1], int(i.split()[2]), int(i.split()[3])])
            else:
                geometry[0] = i.split()[0]
                geometry[1] = i.split()[1]
                geometry[2] = int(i.split()[2])
                geometry[3] = int(i.split()[4])
    print(algebra)
    print(geometry)










