from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import threading

# class IPWebCam(object):
# 	def __init__(self):
# 		self.url = "http://170.233.149.121:8083/webcapture.jpg?command=snap&channel=1?0"

# 	def __del__(self):
# 		cv2.destroyAllWindows()

# 	def get_frame(self):
# 		imgResp = urllib.request.urlopen(self.url)
# 		imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
# 		img= cv2.imdecode(imgNp,-1)
# 		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 		resize = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LINEAR) 
# 		frame_flip = cv2.flip(resize,-1)
# 		ret, jpeg = cv2.imencode('.jpg', img)
# 		return jpeg.tobytes()

# import cv2

class IPWebCam(object):

	def __init__(self):
		self.video = cv2.VideoCapture("http://138.186.1.11:8000/mjpg/video.mjpg")
		(self.grabbed, self.frame) = self.video.read()
		threading.Thread(target=self.update, args=()).start()
	def update(self):
		while True:
			(self.grabbed, self.frame) = self.video.read()
	def __del__(self):
		video.destroyAllWindows()

	def get_frame(self):
		image = self.frame
		_, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()

    

# from django.views.decorators import gzip
# from django.http import StreamingHttpResponse
# import cv2


# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
