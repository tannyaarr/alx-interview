#!/usr/bin/python3
""""Script that reads stdin line by line and  computes metrics"""


import sys
import signal
import re

# Initialize variables to store total file size and status code counts
total_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')


def print_statistics():
    """Prints the statistics of total file size and status code counts."""
    global total_size, status_code_counts
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handles the SIGINT signal (CTRL + C)
    to print statistics before exiting."""
    print_statistics()
    sys.exit(0)


# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Match the line with the log pattern
        match = log_pattern.match(line)
        if match:
            # Extract status code and file size from the matched groups
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update total file size
            total_size += file_size

            # Update the count for the status code if it's one of the expected
            # codes
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except Exception as e:
    # Handle any unexpected exceptions
    print(f"Error processing input: {e}")

# Print the final statistics after processing all input
print_statistics()
