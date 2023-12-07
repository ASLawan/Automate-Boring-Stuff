#!/usr/bin/python3

import time, sys

indent = 0
increase_indent = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if increase_indent:
            indent += 1
            if indent == 20:
                increase_indent = False
        else:
            indent -= 1
            if indent == 0:
                increase_indent = True
except KeyboardInterrupt:
    sys.exit()
