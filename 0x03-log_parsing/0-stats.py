#!/usr/bin/env python3
"""
This module reads from standard input and computes metrics from the log file.
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print the total file size and the status codes.
    """
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """
    Parse a line from the log file.
    """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (IndexError, ValueError):
        return None, None, None

def main():
    """
    Main function for reading from standard input.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is None:
                continue

            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    """
    Main entry point for the script.
    """
    main()