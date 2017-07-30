
def check_sum(min, max):
    list = []
    with open('log.txt', 'r') as f:
        log_list = f.readlines()
    for el in log_list:
        if el.find('umber') == -1:
            if el.find("esult") == 1:
                if el.find('/n') == 0:
                    sum_read = int(el[8:-1])
                else : sum_read = int(el[8:])
                assert sum_read == count_sum(list),"GHHHHH" + str(list)
                list.clear()
                continue
            else:
                new_str = el[7:-1]
                for num in new_str:
                    if num != ' ':
                        list.append(int(num))
                assert min <= len(list) <= max, "Count dieses is wrong when list is " + str(el)
    print('No errors were found')


def count_sum(rec_list):
    sum = 0
    if rec_list != [1,2,3,4,5]:
        for el in rec_list:
            if el == 5:
                sum = sum + 5
            elif el == 1:
                sum = sum + 10
    else: sum = 150
    return sum


check_sum(1,4)