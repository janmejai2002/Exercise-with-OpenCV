# Exercise-with-OpenCV

A super fun game you can play to exercise using your webcam.

This is still in development and has not been completed.

## Install

    pip install -r requirements.txt

You might need to use `pip3`.

## Play

    python main.py

> Commandline arguments

    -h, --help            show this help message and exit
    -w WEBCAM, --webcam WEBCAM
                        Webcam source, if 0 does not work try changing to 1,
                        external webcams might register on 1
    -d DIFFICULTY, --difficulty DIFFICULTY
                        Control how fast circles spawn. Default 60. Increase
                        to make game easier and decrease to make it harder.