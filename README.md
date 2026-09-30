# Obsolete AI Hand Tracker

This repository preserves the classic, lightweight implementation of a real-time computer vision hand tracker built using Python, OpenCV, and Google MediaPipe. 
This repo is an attempt of the very popular computer vision hand tracker seen all over social media last year. Utilizes Python, OpenCV, and MediaPipe


While this exact codebase was the industry standard for lightweight CPU hand tracking throughout 2024 and 2025, Google  restructured the framework in their modern releases. 


## The Legacy Stack (How it used to work)
* **OpenCV (`opencv-python`)** handled parsing the local webcam buffer and rendering the desktop window matrix.
* **MediaPipe (`mediapipe`)** unpacked 21 skeleton landmarks at 30+ FPS without needing a local GPU footprint.

## How to set up an Archival Environment
To simulate or compile this architecture as it existed before the updates, you must force an older environment version
