import cv2
import numpy as np

from object_detector import *

# Load Detector
detector = Detector()

# Load Image
img = cv2.imread('data/vaca3.jpg',1)
height, width = img.shape[:2]
print(height,width)

# Detect objects
contour = detector.detect_objects(img)

# Draw objects boundaries
for cnt in contour:

    area = cv2.contourArea(cnt)
  
    
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect
    
    # Get angle
    if w < h:
        angle = 90 - angle
    else:
        angle = 180 - angle

    if(angle != 5.042449951171875):
        # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.int0(box)
    

        # cv2.circle(img, (int(x),int(y)), 5, (0, 0, 255), -1 )
        # Coordinate points
        cv2.circle(img, (3,126), 5, (0, 0, 255), -1 )
        cv2.circle(img, (496,147), 5, (0, 0, 255), -1 )
        cv2.circle(img, (1,299), 5, (0, 0, 255), -1 )
        cv2.circle(img, (497,296), 5, (0, 0, 255), -1 )

        # Input and Output Coordinates
        pts1 = np.float32([[3,126],[496,147],[1,299],[497,296]])
        pts2 = np.float32([[0,0],[500,0],[0,300],[500,300]])
      
        # Perspective Transform
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, matrix ,(width, height))

        cv2.polylines(img, [box], True,(0,255,0),2)
        cv2.putText(img, "Angle {} r".format(round(angle,1)), (int(x - 100),int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (200, 100, 0), 2)

        rows,cols = img.shape[:2]
        img_result = cv2.resize(img, (round(rows*1.5), round(cols*1.5)), interpolation=cv2.INTER_AREA)

cv2.imshow('Vaca no cio', img)
# cv2.imshow('Perspective transformation', result)
cv2.waitKey(0)
    

