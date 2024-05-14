#!/usr/bin/python3
""""Script that reads stdin line by line and  computes metrics"""


import sys
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                      500: 0}
line_count = 0


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


def print_statistics():
    global total_file_size
    global status_code_counts

    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()

    parts = line.split()
    if len(parts) != 7:
        continue
    ip_address, _, _, status_code_str, file_size_str = parts
    try:
        status_code = int(status_code_str)
        file_size = int(file_size_str)
    except ValueError:
        continue

    total_file_size += file_size
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1

    line_count += 1

    if line_count % 10 == 0:
        print_statistic()
