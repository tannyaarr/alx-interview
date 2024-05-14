#!/usr/bin/python3
""""Script that reads stdin line by line and  computes metrics"""


import sys

def parse_line(line):
    try:
        _, _, _, _, status_code, file_size = line.split()
        return int(status_code), int(file_size)
    except ValueError:
        return None, None

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print(f"Total file size: {total_size}")
                    for code in sorted(status_counts.keys()):
                        if status_counts[code] > 0:
                            print(f"{code}: {status_counts[code]}")
                    print()

    except KeyboardInterrupt:
        print("\nKeyboard interruption detected. Printing final statistics:")
        print(f"Total file size: {total_size}")
        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")

if __name__ == "__main__":
    main()