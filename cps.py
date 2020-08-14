def Judge():
    line = input()
    line = line.split(' ')
    n = int(line[0])
    m = int(line[1])
    X = [0]*n
    Y = [0]*n
    C = ['']*n
    for i in range(n):
        line = input()
        line = line.split(' ')
        X[i] = int(line[0])
        Y[i] = int(line[1])
        C[i] = line[2]
    res = ['Yes']*m
    for mm in range(m):
        line = input()
        line = line.split(' ')
        t = int(line[0])
        tx = int(line[1])
        ty = int(line[2])
        if n == 0:
            break
        if t + tx * X[0] + ty * Y[0] > 0 and C[0] == 'A':
            map = {True: 'A', False:'B'}
        elif t + tx * X[0] + ty * Y[0] > 0 and C[0] == 'B':
            map = {True: 'B', False:'A'}
        elif t + tx * X[0] + ty * Y[0] < 0 and C[0] == 'B':
            map = {True: 'A', False:'B'}
        else:
            map = {True: 'B', False:'A'}
        for nn in range(n):
            if t+tx*X[nn]+ty*Y[nn] > 0 and C[nn] == map[True]:
                continue
            elif t+tx*X[nn]+ty*Y[nn] < 0 and C[nn] == map[False]:
                continue
            else:
                res[mm] = 'No'
                break
    for r in res:
        print(r)
    return


if __name__ == '__main__':
    Judge()