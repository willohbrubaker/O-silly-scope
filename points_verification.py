#!/usr/bin/env python3

"""
draw_points.py
Reads lines of the form "(x, y)," from a text file and plots them in order.
Usage:
    python3 draw_points.py points.txt
"""

import sys
import re
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 draw_points.py points.txt", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        data = f.readlines()

    pattern = r"\(\s*([0-9\.\-]+)\s*,\s*([0-9\.\-]+)\s*\)"

    points = []
    for line in data:
        match = re.search(pattern, line)
        if match:
            x_val, y_val = match.groups()
            x_val, y_val = float(x_val), float(y_val)
            points.append((x_val, y_val))

    if not points:
        print("No valid points found in file!")
        sys.exit(1)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, marker='o', linestyle='-', color='pink')

    plt.axis('equal')

    plt.title("Preview of Points from {}".format(filepath))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
