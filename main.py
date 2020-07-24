def sushubiao(x):
    r = [2]
    for j in range(3,x + 1):
        flag = 1
        for i in range(len(r)):
            if j % r[i] == 0:
                flag = 0
                break
        if flag == 1:
            r.append(j)
    return r
print(sushubiao(100000))
