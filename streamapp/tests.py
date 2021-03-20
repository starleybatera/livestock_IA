import cv2
cap = cv2.VideoCapture('http://138.186.1.11:8000/mjpg/video.mjpg')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)
  return frame
  if cv2.waitKey(1) == 27:
    exit(0)