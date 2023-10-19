#!/usr/bin/python3

import sys
import signal

def compute_metrics(lines):
    total_size = 0
    status_codes = {}

    for line in lines:
        parts = line.split()
        if len(parts) != 9:
            continue

        ip, _, _, status, size = parts[0], parts[8], parts[10], parts[12], parts[13]
        if status.isnumeric():
            status = int(status)
        else:
            continue

        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status in status_codes:
                status_codes[status] += 1
            else:
                status_codes[status] = 1

        if size.isnumeric():
            total_size += int(size)

    return total_size, status_codes

def print_metrics(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for status in sorted(status_codes):
        print(f"{status}: {status_codes[status]}")

lines = []
count = 0

def signal_handler(sig, frame):
    global count
    count += 1
    print_metrics(*compute_metrics(lines))
    if count == 10:
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    lines.append(line)
    if len(lines) == 10:
        print_metrics(*compute_metrics(lines))
        lines = []

print_metrics(*compute_metrics(lines))
