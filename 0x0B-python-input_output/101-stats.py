#!/usr/bin/python3
"""Script reads stdin line by line and computes terics
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
try:
    total_size = 0
    input_codes = []
    for index, line in enumerate(sys.stdin, 1):
        if line:
            line = line.split()
            if len(line) > 2:
                if line[-1].isnumeric() and line[-2].isnumeric():
                    fsize = line[-1]
                    status = line[-2]
                    total_size += int(fsize)
                if len(status) > 0 and int(status) in status_codes:
                    input_codes.append(int(status))
                if index % 10 == 0:
                    print(f'File size: {total_size}')
                    for i in status_codes:
                        if i in input_codes:
                            status_count = input_codes.count(i)
                            print(f'{i}: {status_count}')
except Exception:
    pass
finally:
    print(f'File size: {total_size}')
    for i in status_codes:
        if i in input_codes:
            status_codes = input_codes.count(i)
            print(f'{i}: {status_count}')
