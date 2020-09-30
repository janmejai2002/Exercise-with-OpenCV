import cv2
import time
import random
import argparse
from imutils.video import VideoStream
import numpy as np
import copy

ap = argparse.ArgumentParser()

ap.add_argument("-w", "--webcam", type=int, default=0, help="Webcam source, if 0 does not work try changing \
    to 1, external webcams might register on 1")
ap.add_argument("-d", "--difficulty", type=int, default=60, help="Control how fast circles spawn. Default 60. Increase to make game easier \
    and decrease to make it harder")
args = vars(ap.parse_args())

# constants
isBgCaptured = 0
bgSubThreshold = 60
learningRate = 0
bgModel = None


def remove_background(frame, bgModel, lr):
    """
    To remove background from captured region.
    Parameters:
    frame: Frame/Image
    bgModel: Background Subraction Model 
    lr: Learning Rate for bgModel
    """
    fgmask = bgModel.apply(frame, learningRate=lr)
    kernel = np.ones((2, 2), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=2)
    fgmask = cv2.dilate(fgmask, None, iterations=2)

    removed_bg = cv2.bitwise_and(frame, frame, mask=fgmask)
    # convert to binary image
    gray = cv2.cvtColor(removed_bg, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('grayscale', gray)
    blur = cv2.GaussianBlur(gray, (11, 11), 0)

    ret, thresh = cv2.threshold(
        blur, 60, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('mask', thresh)
    return thresh


print("[INFO] Initializing webcam ...")
vs = VideoStream(src=args["webcam"]).start()
time.sleep(1)
frame_base = vs.read()
print(f"Frame dimensions : {frame_base.shape[1]}x{frame_base.shape[0]}")

frame_counter = 0
# game properties
while True:
    frame = vs.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", frame)
    frame_circle = copy.deepcopy(frame)
    # RGN for every 5 frames
    if frame_counter % 60 == 0:
        center = (random.randint(
            20, frame_base.shape[1]-20), random.randint(20, frame_base.shape[0]-20))
        radius = random.randint(10, 30)
        circle_color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    frame_circle = cv2.circle(frame_circle, center=center, radius=radius,
                              color=circle_color, thickness=-1, lineType=8)

    # print(frame_counter)
    cv2.imshow("Frame Circle", frame_circle)

    if isBgCaptured == 1:
        thresh = remove_background(frame, bgModel, learningRate)

    frame_counter += 1
    key = cv2.waitKey(10) & 0xFF
    if key == ord('q'):
        break

    if key == ord('b'):
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
        time.sleep(0.5)
        isBgCaptured = 1
        print('Background Captured')
