def prufer_code ():
    x = int(input('Nhập số cạnh:'))
    D1 = [[None]*x for i in range(x+1)]
    Dk = [[i, 0] for i in range(x+1)]
    L = []
    for i in range(x):
        v1, v2 = [int(x) for x in input('Nhập cạnh %d trên một dòng:'%(i+1)).split()]
        D1[v1][Dk[v1][1]] = v2
        D1[v2][Dk[v2][1]] = v1
        Dk[v1][1] += 1
        Dk[v2][1] += 1
    Dk[0][1] = 100
    for i in range(x+1):
        v = min(Dk, key=lambda e: 10*e[1]+e[0])[0]
        n = D1[v]
        L.append(v)
        Dk[v][1] = 1000
        for ii in n:
            if ii is None:
                break
            D1[ii].remove(v)
            Dk[ii][1] = Dk[ii][1] - 1
    return L


print(prufer_code())

