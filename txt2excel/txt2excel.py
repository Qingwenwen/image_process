import xlwt


FILE_PATH = r'.\score_data.txt'
XLS_FILE = r'.\Score_data.xls'


def make_title():
    return [
        '名字',
        '出生日期',
        '最好成绩',
        '第二名成绩',
        '第三名成绩',
        '最差成绩'
    ]


def shape_time(time):
    time = time.replace('-', ':')
    time = time.replace('.', ':')
    return time


def shape_all_time(data):
    new_data = list()
    for one_line in data:
        time_data = one_line[2:]
        for j in range(len(time_data)):
            time_data[j] = shape_time(time_data[j])
        temp_list = one_line[0:2] + time_data
        new_data.append(temp_list)
    return new_data


def get_data(filename):
    all_data = []
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            data = line.rstrip("\n").split(',')
            all_data.append(data)
    return all_data


def make_table(title, data):
    data.insert(0, title)
    return data


def write2excel(path, value):
    file = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = file.add_sheet('data')
    for i in range(len(value)):
        for j in range(len(value[i])):
            sheet.write(i, j, value[i][j])
    file.save(path)


def main():
    data = get_data(FILE_PATH)
    data = shape_all_time(data)
    title = make_title()
    table = make_table(title, data)
    write2excel(XLS_FILE, table)


main()
