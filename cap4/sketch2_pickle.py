#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import os
import pickle

man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data2.txt', 'wb') as man_file, open('other_data2.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except pickle.PickeError as err:
    print('Pickling error: ' + str(err))
