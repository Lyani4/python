# https://inf-ege.sdamgia.ru/problem?id=18430
print('x y z w')
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if not ((a and b) or (b == c) or d):
                    print(a, b, c, d)
