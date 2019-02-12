def shape_time(time):
    time = time.replace('-', ':')
    time = time.replace('.', ':')
    return time


def main():
    test_list = ['2.35', '3-56']
    for time in range(len(test_list)):
        test_list[time] = shape_time(test_list[time])
    print(test_list)


main()
