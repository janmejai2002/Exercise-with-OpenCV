# Exercise-with-OpenCV

A super fun game you can play to exercise using your webcam.

This is still in development and has not been completed.

## For Contributing

The aim is to basically use HSV ranges. The player will say have color X band tied to their hand. Then the video stream is thresholded using inRange and the centre coordinate of player's hand is detected. This coordinate is matched with the centre of a ball spawn. If they match, then user gets a +1 in score. 

Tasks to be completed  
- [ ] Implement inRange.  
- [ ] Implement scoring  
- [ ] Implement Game UI  
- [ ] Bug Testing.  

Additional features which can be implemented  :

- [ ] The circles spawn by starting from a small point and increase in size over a period of time and then decrease to zero, unless player scores a point.


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
