import cv2
import numpy as np


class crop:
    cropping = False
    doneCropping = False
    roi = None
    oriImage = None
    x_start, y_start, x_end, y_end = 0, 0, 0, 0

    def __init__(self, image):
        global oriImage
        oriImage = image.copy()

    def mouse_crop(self, event, x, y, flags, param):
        # grab references to the global variables
        global x_start, y_start, x_end, y_end, cropping, roi, doneCropping

        # if the left mouse button was DOWN, start RECORDING
        # (x, y) coordinates and indicate that cropping is being
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x_start, self.y_start, self.x_end, self.y_end = x, y, x, y
            self.cropping = True

        # Mouse is Moving
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.cropping == True:
                self.x_end, self.y_end = x, y

        # if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates
            self.x_end, self.y_end = x, y
            self.cropping = False  # cropping is finished

            refPoint = [(self.x_start, self.y_start), (self.x_end, self.y_end)]

            if len(refPoint) == 2:  # when two points were found
                self.roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                self.doneCropping = True

    def start(self, image):
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.mouse_crop)

        while True:

            i = image.copy()

            if (self.doneCropping):
                return self.roi

            if not self.cropping:
                cv2.imshow("image", image)

            elif self.cropping:
                cv2.rectangle(i, (self.x_start, self.y_start), (self.x_end, self.y_end), (255, 0, 0), 2)
                cv2.imshow("image", i)

            cv2.waitKey(1)

        # close all open windows
        # cv2.destroyAllWindows()


def startCropping(image):
    cropobj = crop(image)
    roi_1 = cropobj.start(image)
    return roi_1
