from random import *

file1 = open('int_data.txt', 'w')
for i in range(10**5):
    file1.write(str(randint(0, 100)) + '\n')

file2 = open('float_data.txt', 'w')
for j in range(10**5):
    num = float(int(10000*random()))/100
    file2.write(str(num) + '\n')