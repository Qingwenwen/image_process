import re
import xlwt


def validatetitle(title):
    rstr = r"[\:\.\-]"
    new_title = re.sub(rstr, ":", title)
    return new_title


def read_file(filename):
    all_list1 = []
    with open(filename) as file_object:
        code_list = file_object.readlines()
    for line in code_list:
        line = line.rstrip("\n").split(',')
        all_list1.append(line)
    return all_list1


def str_handle(list1):
    name = []
    mark = []
    for i in list1:
        name.append(i[0])
        mark.append(i[1:])
    for i in mark:
        for x in range(0, len(i)):
            i[x] = validatetitle(i[x].strip())
    sort_list = []
    for i in mark:
        i = sorted(set(i))
        sort_list.extend([i[0], i[1], i[2], i[-1]])
    result_list = []
    result_list.extend([
       '名字',
       '出生日期',
       '最好成绩',
       '第二名成绩',
       '第三名成绩',
       '最差成绩'
    ])
    for i, x in zip(name, sort_list):
        result_list.append(i + x)
    return result_list


def write2excel(path, value):
    file = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = file.add_sheet('data')
    for i in range(0, len(value)):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    file.save(path)


filename1 = r'.\score_data.txt'
list1 = read_file(filename1)
result_list = str_handle(list1)
xlsname1 = r'.\Score_data.xls'
write2excel(xlsname1, result_list)
