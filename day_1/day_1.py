def sum(list_1):
    total: int = 0
    for num in list_1:
        num: int = int(num)
        total += num
    return total


def max(total_list: list):
    largest_number = total_list[0]
    for number in total_list:
        if number > largest_number:
            largest_number = number
    return largest_number


def sort(total_list: list):
    total_list = sorted(total_list)
    return total_list

def cal_count():
    with open('D:/work/file_test.txt', 'r') as f:
        # lines = f.readline()
        lines = [line.rstrip('\n') for line in f]
        # print(lines)
        list_1: list = []
        total_list: list = []
        for line in lines:
            lines = lines[1:]
            list_1.append(line)
            if line == '':
                # print(list_1)
                del list_1[-1]
                total = sum(list_1)
                # print(total)
                total_list.append(total)
                list_1 = []
            if (len(lines)) == 1:
                # print(lines)
                total = sum(lines)
                # print(total)
                total_list.append(total)
    total_list = sort(total_list)
    total_list = (total_list[-3:])
    total_list = sum(total_list)
    print(total_list)

if __name__ == '__main__':
    cal_count()