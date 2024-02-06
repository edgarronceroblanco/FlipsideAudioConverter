# Flipside Audio Converter

## Overview

Flipside Audio Converter is a simple GUI application built with Tkinter and FFmpeg for converting audio files between different formats. It supports FLAC, WAV, AIFF, M4A, and MP3 as input formats, and it can output to M4A, MP3, and FLAC.

## Features

- Convert audio files between different formats.
- Input formats: FLAC, WAV, AIFF, M4A, MP3.
- Output formats: M4A, MP3, FLAC.
- Apply optional dithering for 24 and 32-bit depth files.
- Automatically creates an output folder for converted files.

## Requirements

- Python 3
- FFmpeg

## Getting Started

### Windows

1. Download the repository via ZIP file or run `git clone https://github.com/edgarronceroblanco/flipside-audio-converter.git`.
2. Install Python 3 from the [Microsoft Store]
3. Get the latest stable FFmpeg build from [Gyan Dev](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z).
4. Extract the FFmpeg archive to `C:\Users\Public\ffmpeg`. (The path itself is a directory, it will look like this the C:\Users\Public\ffmpeg\ffmpeg.exe).
5. Add `C:\Users\Public\ffmpeg` to the PATH environment variable.
6. Logout and log back in to your Windows user or reboot the machine.
7. Run FlipsideAudioConverter.py with the Python3 interpreter.

### GNU/Linux Debian-based distributions

1. Download the repository via ZIP file or run `git clone https://github.com/edgarronceroblanco/flipside-audio-converter.git`.
2. Install Python 3 and Tkinter with `sudo apt update; sudo apt install python3 python3-tk`.
3. Install FFmpeg with `sudo apt update; sudo apt install ffmpeg`.
4. Run the application from the terminal: `python3 FlipsideAudioConverter.py`.

## MacOS

1. Download the repository via ZIP file or run `git clone https://github.com/edgarronceroblanco/flipside-audio-converter.git`.
2. Install the latest Python 3.x from [its official webpage](https://www.python.org/downloads/).
3. Download the latest stable FFmpeg build from [evermeet.cx](https://evermeet.cx/ffmpeg/ffmpeg-6.1.1.7z).
4. Extract FFmpeg into `/usr/local/bin` directory.
5. Run the application from the terminal: `python3 FlipsideAudioConverter.py`.
