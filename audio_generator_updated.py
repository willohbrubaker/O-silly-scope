#!/usr/bin/env python3
"""
points_to_audio.py
Read (x, y) points from a text file and create a 16-bit stereo WAV file.
Usage:
    python3 points_to_audio.py points.txt output.wav
"""

import sys
import re
import wave
import struct

SAMPLE_RATE = 44100  # standard audio CD rate
AMP_16BIT_MAX = 32767

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 points_to_audio.py <points.txt> <output.wav>")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    points = parse_points_file(in_file)
    if not points:
        print("No valid points found in file!")
        sys.exit(1)

    # Scale points to 16-bit range
    scaled_points = scale_points(points)

    write_stereo_wav(scaled_points, out_file)
    print(f"Successfully wrote {len(scaled_points)} stereo samples to '{out_file}'.")

def parse_points_file(filename):
    """
    Read lines like '(x, y),' or '(x, y)' from filename.
    Return a list of (float, float).
    """
    pattern = r"\(\s*([0-9\.\-]+)\s*,\s*([0-9\.\-]+)\s*\)"
    points = []
    with open(filename, "r") as f:
        for line in f:
            matches = re.findall(pattern, line)
            for (x_str, y_str) in matches:
                x_val = float(x_str)
                y_val = float(y_str)
                points.append((x_val, y_val))
    return points

def scale_points(points):
    """
    Scale all x, y to fit in the range [-32767, 32767].
    """
    max_val = 0
    for (x, y) in points:
        max_val = max(max_val, abs(x), abs(y))

    if max_val == 0:
        return [(0, 0) for _ in points]

    scale_factor = AMP_16BIT_MAX / max_val
    scaled = []
    for (x, y) in points:
        sx = int(x * scale_factor)
        sy = int(y * scale_factor)
        # Clip in case rounding goes out of bounds
        sx = max(min(sx, AMP_16BIT_MAX), -AMP_16BIT_MAX)
        sy = max(min(sy, AMP_16BIT_MAX), -AMP_16BIT_MAX)
        scaled.append((sx, sy))
    return scaled

def write_stereo_wav(scaled_points, out_filename):
    """
    Write a 16-bit stereo WAV file at SAMPLE_RATE with scaled_points.
    Left channel = x, Right channel = y.
    """
    with wave.open(out_filename, "wb") as wav_file:
        # 2 channels, 2 bytes per sample, 44.1kHz
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(SAMPLE_RATE)

        # Build raw bytes from the scaled points
        # Each frame: (left_sample, right_sample) as 16-bit little-endian
        frames = bytearray()
        for (x, y) in scaled_points:
            frames += struct.pack("<h", x)  # left
            frames += struct.pack("<h", y)  # right

        wav_file.writeframes(frames)

if __name__ == "__main__":
    main()
