def list_example():
    # пример работы list
    # 0 1 2 3 - индексы
    a = [3, 4, 6, 8]
    for index in range(len(a)):
        print(a[index], index)
    # распечать 3 элемент из а
    print(a[2])


def dict_example():
    # 1 7.2 индекс - индексы
    b = {1: "zae5", 7.2: 7.2, 'индекс': 'значение'}
    for key in b:
        print(key, b[key])
    print(b['индекс'])
    print(b[7.2])


if __name__ == '__main__':
    print('list ----------')
    list_example()
    print('dict ------------')
    dict_example()
