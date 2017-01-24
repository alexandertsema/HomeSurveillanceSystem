# HomeSurveillanceSystem

## Overview

This project implements very simple multithreading system for video surveillance which can be used at home with laptop and web camera or with Raspberry Pi and CSI camera. The system has the ability to detect motions and notify user about that.

### Architecture

The system consists of 3 Managers running in separate threads:

1. VideoManager.py - responsible for saving captured video frames to file
2. AudioManager.py - responsible for saving captured audio frames to file
3. MergeManager.py - responsible for merging video and audio signals.

### Motivation

I was always curious what is my dog doing when I'm at work.

## Tech stack

* Python 3.6
* OpenCV-Python
* Pyaudio
* Ffmpeg

### Tools

* PyCharm 2016

## Issues

* The system is sensitive to light
* Video and audio signals are not synchronized

## Future work

* Bug fixing
* Saving day data to cloud
* Notifying user about motion detected
* Streaming signals via UDP in real time