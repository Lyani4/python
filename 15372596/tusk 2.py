# https://inf-ege.sdamgia.ru/problem?id=33504

print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not (((x == (not y)) <= (y and (not z))) or (z and (not w))):
                    print(x, y, z, w)