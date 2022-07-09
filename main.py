h = (0, 0)
for i in range(1, 10000):
    s = i
    while s != 1:
        if s % 2 == 0:
            s = int(s / 2)
            print(i, s)
        else:
            s = int((s*3)+1)
            if s > h[1]:
                h = (i, s)
            print(i, s)
print(h)
