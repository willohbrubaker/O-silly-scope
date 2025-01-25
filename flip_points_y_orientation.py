#!/usr/bin/env python3
"""
parse_and_flip.py
Reads lines of the form "(x, y)," from a text file, flips the Y value,
and writes them back out. Default output is to stdout, or specify an output file.
Usage:
    python3 parse_and_flip.py points.txt [flipped_points.txt]
"""

import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: parse_and_flip.py points.txt [flipped_points.txt]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    pattern = r"\(\s*([0-9\.\-]+)\s*,\s*([0-9\.\-]+)\s*\)"

    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        match = re.search(pattern, line)
        if match:
            x_str, y_str = match.groups()
            x_val = float(x_str)
            y_val = float(y_str)

            # Flip Y
            y_val = -y_val

            new_lines.append(f"({x_val}, {y_val}),\n")
        else:
            new_lines.append(line)

    if output_file:
        with open(output_file, 'w') as out:
            out.writelines(new_lines)
        print(f"Flipped points written to {output_file}")
    else:
        for ln in new_lines:
            print(ln, end='')

if __name__ == "__main__":
    main()
