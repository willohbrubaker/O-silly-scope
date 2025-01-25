#!/usr/bin/env python3
"""
Flatten an SVG into line segments (M/L only) and print the points as Python tuples.
Requires 'svgpathtools': pip install svgpathtools
"""

import sys
import math
from svgpathtools import svg2paths, Line, CubicBezier, QuadraticBezier, Arc

# Number of line segments to use when flattening each curve
# Higher = more precision, more points
FLATTEN_STEPS = 20

def flatten_segment(segment, steps=FLATTEN_STEPS):
    """
    Given a segment (Line, CubicBezier, QuadraticBezier, or Arc),
    return a list of points approximating it as line segments.
    """
    points = []
    for i in range(steps + 1):
        t = i / steps  # param from 0 to 1
        pt = segment.point(t)
        points.append((pt.real, pt.imag))
    return points

def flatten_path(path, steps=FLATTEN_STEPS):
    """
    Flatten an entire path (sequence of segments).
    Returns a list of (x, y) points approximating the path.
    """
    all_points = []
    for segment in path:
        seg_points = flatten_segment(segment, steps=steps)
        # On each new segment, we'd be duplicating the last point of previous
        # segment as first point of next segment. Let's skip duplicates:
        if all_points and seg_points:
            # Compare last point in all_points to first in seg_points
            if math.isclose(all_points[-1][0], seg_points[0][0], abs_tol=1e-9) and \
               math.isclose(all_points[-1][1], seg_points[0][1], abs_tol=1e-9):
                seg_points = seg_points[1:]
        all_points.extend(seg_points)
    return all_points

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <svgfile.svg> [flatten_steps]".format(sys.argv[0]),
              file=sys.stderr)
        sys.exit(1)

    svgfile = sys.argv[1]
    if len(sys.argv) >= 3:
        # Optional override of flatten steps
        global FLATTEN_STEPS
        FLATTEN_STEPS = int(sys.argv[2])

    # Load all paths (and their attributes if needed)
    paths, attributes = svg2paths(svgfile)

    # We'll store lists-of-lists if there's more than one path
    all_paths_points = []

    for i, path in enumerate(paths):
        flattened = flatten_path(path, steps=FLATTEN_STEPS)
        all_paths_points.append(flattened)

        print(f"# Path {i+1}")
        for p in flattened:
            print(f"  {p},")

    print("\n# Done. Copy/paste these points into your code as needed.")

if __name__ == "__main__":
    main()
