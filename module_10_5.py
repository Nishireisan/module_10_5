import multiprocessing
import time
import threading


def read_info(name):
    all_data = []

    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start_time = time.time()
#
# read_info('file 1.txt')
# read_info('file 2.txt')
# read_info('file 3.txt')
# read_info('file 4.txt')
#
# end_time = time.time()
#
# print(f'{end_time-start_time:6f} секунд')


if __name__ == '__main__':
    start_time_proc = time.time()

    pool = multiprocessing.Pool()
    with pool:
        map(read_info, filenames)

    end_time_proc = time.time()

    print(f'{end_time_proc-start_time_proc:6f} секунд')
