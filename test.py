import time

if __name__ == '__main__':
    start_time = time.time()
    a = 0
    for i in range(0, 1_000_000_000):
        a = a + 1
    print(f'Время выполнения {time.time() - start_time}')
