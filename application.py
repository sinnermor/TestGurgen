import subprocess
import pytest
import os

import sys

def get_file_name():
    print('Please type gurgen version')
    file_name = input()
    return file_name

def run_code(name, cout_pfases, from_count, to_count):
    f = open('log.txt', 'a')
    sys.stdout =f
    sys.stdout.flush()
    command = './gurgen_files/' + name + ' ' + str(cout_pfases) + ' ' + str(from_count) +' ' + str(to_count)
    # os.system()
    try:
        direct_output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        direct_output = e.output
    test = str(direct_output, 'utf-8')
    print(test)


def run_popen(name, cout_pfases, from_count, to_count):
    command = './gurgen_files/' + name
              # + ' ' + str(cout_pfases) + ' ' + str(from_count) + ' ' + str(to_count)
    process = subprocess.Popen([command , str(cout_pfases),str(from_count),str(to_count)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    returncode = process.wait()
    # print('Code is {0}'.format(returncode))
    return str(process.stdout.read(), 'utf-8')
    # return process

def decode_responce(responce):
    pass

def check_sum(array, fin_sum):
    sum = 0
    for el in array:
        if el == 5:
            sum = sum + 5
        elif el == 1:
            sum = sum + 10
    assert sum == fin_sum, 'Sums are different' + sum + ' != ' + fin_sum

def parse_response(response_string):
    index = response_string.find('Dieses')
    mass = response_string[index+7 :]
    print('MASSS' + mass)
    part = response_string.rpartition('Result')
    print('MUUUU')


te = run_popen('gurgen_0', 10, 1, 4)
parse_response(te)
