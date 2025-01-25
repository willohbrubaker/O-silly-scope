# O-silly-scope

O-silly-scope is a proof-of-concept project for generating visuals on an XY oscilloscope using stereo audio signals. By converting audio files into voltage signals, this project explores how sound can create striking patterns and designs on a physical oscilloscope.

While currently a personal experiment, O-silly-scope has the potential to be developed into a reusable package for creative audio-visual explorations.

Overview
This project demonstrates:

Audio-to-Visual Transformation: Creating XY oscilloscope visuals directly from stereo audio files.
Basic Signal Handling: Converting stereo waveforms into X and Y axis signals suitable for oscilloscope input.
Goals
The primary goal of this project is experimentation, but the long-term vision includes:

Packaging as a library for broader use.
Adding features for signal manipulation and visualization customization.
Getting Started
Requirements
To run the current proof of concept, you’ll need:

An oscilloscope with XY input capabilities.
A computer capable of audio output and Python scripting.
Dependencies
Install the following Python libraries before running the project:

bash
Copy
Edit
pip install numpy scipy matplotlib
Running the Project
Clone this repository:

bash
Copy
Edit
git clone https://github.com/willohbrubaker/O-silly-scope.git
cd O-silly-scope
Prepare an audio file for input. Ensure it’s a stereo file where:

The left channel represents the X-axis signal.
The right channel represents the Y-axis signal.
Run the main script:

bash
Copy
Edit
python main.py your_audio_file.wav
Connect your computer's audio output to the oscilloscope's XY input and adjust the oscilloscope's settings for visualization.

Current Limitations
Early Stage: The project is not yet a fully-featured package or library.
Manual Setup: Limited user interface and requires familiarity with Python and audio handling.
File Compatibility: Supports basic stereo audio formats; compatibility with other formats is untested.
Future Development
Some ideas for future iterations:

Developing a more user-friendly interface.
Packaging as a Python library.
Adding features for waveform generation, pattern manipulation, and real-time control.
Contributing
Since this is an exploratory project, contributions are currently informal. However, feedback and ideas are always welcome! Fork the repository and share your suggestions via pull requests or issues.

License
This project is available under the MIT License. See the LICENSE file for more information.

Additional Notes
This is a personal experiment, and results may vary depending on your oscilloscope's settings and capabilities.
Start with lower audio volumes to avoid hardware damage.
