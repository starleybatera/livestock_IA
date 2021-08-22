
# VIDEO

import cv2
import numpy as np

from object_detector import *


# Load Detector
detector = Detector()

# Load Video
cap = cv2.VideoCapture('data/cows_cio.mov')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 416)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 416)

while True:
    _, img = cap.read()

    # Detect objects
    contour = detector.detect_objects(img)

    # Draw objects boundaries
    for cnt in contour:
        
        # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        # Get angle
        if w < h:
            angle = 90 - angle
        else:
            angle = 180 - angle
        print("Angulo "+angle)

        # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.int0(box)


        cv2.circle(img, (int(x),int(y)), 5, (0, 0, 255), -1 )

        # Coordinate points
        # cv2.circle(img, (9,13), 5, (0, 0, 255), -1 )
        # cv2.circle(img, (600,14), 5, (0, 0, 255), -1 )
        # cv2.circle(img, (4,600), 5, (0, 0, 255), -1 )
        # cv2.circle(img, (600,600), 5, (0, 0, 255), -1 )

        # Input and Output Coordinates
        pts1 = np.float32([[9,13],[600,14],[4,600],[600,600]])
        pts2 = np.float32([[0,0],[600,0],[0,600],[600,600]])

        # Perspective Transform
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, matrix , (400, 600))

        
        cv2.polylines(img, [box], True,(0,255,0),2)
        cv2.putText(img, "{} degrees".format(round(angle,1)), (int(x - 100),int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (200, 100, 0), 2)

        rows,cols = img.shape[:2]
        img_result = cv2.resize(img, (round(600), round(600)), interpolation=cv2.INTER_AREA)

    cv2.imshow('Vaca no cio', img_result)
    # cv2.imshow('Perspective Transformation',result)
    key = cv2.waitKey(1)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
