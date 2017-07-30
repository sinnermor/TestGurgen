import subprocess
import pytest
import os

import sys


class Gurgen():

    def __init__(self, iter, min, max):
        self.name = self.get_file_name()
        self.count_iteratoin = iter()
        self.min_count = min
        self.max_count = max

    def get_file_name(self):
        print('Please type gurgen version')
        file_name = input()
        return file_name

    # def run_code(name, cout_pfases, from_count, to_count):
    #     f = open('log.txt', 'a')
    #     sys.stdout =f
    #     sys.stdout.flush()
    #     command = './gurgen_files/' + name + ' ' + str(cout_pfases) + ' ' + str(from_count) +' ' + str(to_count)
    #     # os.system()
    #     try:
    #         direct_output = subprocess.check_output(command, shell=True)
    #     except subprocess.CalledProcessError as e:
    #         direct_output = e.output
    #     test = str(direct_output, 'utf-8')
    #     print(test)


    def run_popen(self, from_count, to_count):
        command = './gurgen_files/' + self.name
        # + ' ' + str(cout_pfases) + ' ' + str(from_count) + ' ' + str(to_count)
        process = subprocess.Popen([command, str(self.count_iteratoin), str(self.min_count), str(self.max_count)],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        returncode = process.wait()
        # print('Code is {0}'.format(returncode))
        final_string = process.stdout.read()
        return (final_string.decode('utf-8'))
        # return process

    def decode_responce(responce):
        pass

    def parse_response(self, response_string):
        index = response_string.find('Dieses')
        mass = response_string[index + 7:]
        print('MASSS' + mass)
        part = response_string.rpartition('Result')
        print('MUUUU')

    def check_sum(self, min, max):
        list = []
        with open('log.txt', 'r') as f:
            log_list = f.readlines()
        for el in log_list:
            if el.find('umber') == -1:
                if el.find("esult") == 1:
                    if el.find('/n') == 0:
                        sum_read = int(el[8:-1])
                    else:
                        sum_read = int(el[8:])
                    assert sum_read == self.count_sum(list), 'Sums are different' + sum_read + ' != ' + self.count_sum(list)
                    list.clear()
                    continue
                else:
                    new_str = el[7:-1]
                    for num in new_str:
                        if num != ' ':
                            list.append(int(num))
                    assert min <= len(list) <= max, "Count dieses is wrong when list is " + str(el)
        print('No errors were found')

    def count_sum(self, rec_list):
        sum = 0
        if rec_list != [1, 2, 3, 4, 5]:
            for el in rec_list:
                if el == 5:
                    sum = sum + 5
                elif el == 1:
                    sum = sum + 10
        else:
            sum = 150
        return sum

    def destroy(self):
        pass

