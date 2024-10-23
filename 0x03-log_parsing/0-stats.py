#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re

def print_metrics(status_counts, total_size):
    """
    Args:
        status_counts : Dictionary containing status codes and their counts.
        total_size : The total file size.

    return:
        the file size and the number of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                 '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_counter = 0

try:
    for log_line in sys.stdin:
        line_counter += 1

        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', log_line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))

            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            
            if line_counter % 10 == 0:
                print_metrics(status_counts, total_file_size)

except KeyboardInterrupt:
    print_metrics(status_counts, total_file_size)
    sys.exit(0)

print_metrics(status_counts, total_file_size)
