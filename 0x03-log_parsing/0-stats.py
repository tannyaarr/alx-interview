#!/usr/bin/python3
""""Script that reads stdin line by line and  computes metrics"""


import sys

def parse_line(line):
    try:
        _, _, _, _, status_code, file_size, = line.split()
        return int(status_code), int(file_size)
    except ValueError:
        return None, None
    
def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i %10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_counts.keys()):
                    print(f"{code}: {status_counts[code]}")

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()