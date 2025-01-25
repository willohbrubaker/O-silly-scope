#!/usr/bin/env python3
"""
loop_audio.py
Play an audio file continuously in an infinite loop

"""

import pygame
import time
import sys

AUDIO_FILE = "audio.wav"  # Replace with your actual file name

def main():
    pygame.mixer.init(frequency=44100, size=-16, channels=2)
    pygame.mixer.music.load(AUDIO_FILE)

    # loops = -1 means infinite
    pygame.mixer.music.play(loops=-1)

    print(f"Playing {AUDIO_FILE} in an infinite loop. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping playback...")
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit(0)

if __name__ == "__main__":
    main()
