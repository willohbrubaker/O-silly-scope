# O-silly-scope

O-silly-scope is a proof-of-concept project for generating visuals on an XY oscilloscope using stereo audio signals. By converting audio files into voltage signals, thproject explored how sound can create patterns and designs on a physical oscilloscope.

While this a personal experiment, O-silly-scope could be further developed into a reusable package for creative audio-visual exploration.

## Overview

This project demonstrates:

- **Audio-to-Visual Transformation**: Creating XY oscilloscope visuals directly from stereo audio files.
- **Basic Signal Handling**: Converting stereo waveforms into X and Y axis signals suitable for oscilloscope input.

## Goals

The primary objective of this project was to demonstrate and prove the relationship between stereo and visual dimensions and the ability to translate between sensory mediums. Future vision includes broadening this to:

- Packaging as a library for broader use.
- Adding features for signal manipulation and visualization customization.

## Getting Started

### Requirements

To run the current proof of concept, you’ll need:

- An oscilloscope with XY input capabilities.
- A computer capable of audio output and Python scripting.

> **Note on audio quality**: The quality of your device's audio output is critical. While this worked using my HP Pavilion laptop, it did not work with all computer devices in my home, noteably not with a Raskberry PI 4B. If attempting to recreate these visuals, please keep this in mind and try other devices if needed.

### Dependencies

Install the following Python libraries before running the project:

```bash
pip install numpy scipy matplotlib
```

### Running the Project

Clone this repository:

```bash
git clone https://github.com/willohbrubaker/O-silly-scope.git
cd O-silly-scope
```

**⚠️ Warning**: Start with lower audio volumes to avoid hardware damage!!!
In a terminal window with this project open, run the main script:

```bash
python loop_audio.py
```

Connect your computer's audio output to the oscilloscope's XY input and adjust the oscilloscope's settings for visualization.

## Demo / Examples

While on might further work with the audio generation, etc. to sharpen and refine this project, my objective was took make an audio output which rendered legible text. You can see my output for the channels.wav audio file included in this repository, below! You will notice my configuration in terms of scaling, etc. 

<!-- ![Oscilloscope Demo Image](images/osillyscope-output.png) -->


## Current Limitations

- The project is not yet a fully-featured package or library.
- Limited user interface and requires familiarity with Python, terminal, and audio handling.

## Future Development

Ideas for future iterations:

- Developing a more user-friendly interface.
- Packaging as a Python library.
- Adding features for waveform generation, pattern manipulation, and potentially real-time control.

## Contributing

Since this is an exploratory project, contributions are currently informal. However, feedback and ideas are always welcome! Fork the repository and share your suggestions via pull requests or issues.

## License

This project is available under the MIT License. See the [LICENSE](LICENSE) file for more information.

