import numpy as np
import cv2

cap = cv2.VideoCapture('1.mp4')

fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
	int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

classfier = cv2.CascadeClassifier("databases/haarcascade_frontalface_alt.xml")
c = 1
out = cv2.VideoWriter('encryption.avi',cv2.cv.CV_FOURCC('I','4','2','0'),fps,size)
while(cap.isOpened()):
	ret, frame = cap.read()

	#at first, save picture
	cv2.imwrite('image_decryption/' + str(c) + '.jpg', frame)

	#for i in range(10):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
	#contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#cv2.drawContours(frame, contours, -1, (0,0,255), 8)
	cv2.equalizeHist(gray,gray)

	divisor = 8
	h, w = size
	minSize = (w/divisor, h/divisor)
	faceRects = classfier.detectMultiScale(gray,1.3,2,cv2.CASCADE_SCALE_IMAGE,minSize)
	if len(faceRects)>0:
		for faceRect in faceRects:
			x,y,w,h = faceRect
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),-1)

	#cv2.imshow('frame',frame)
	cv2.imwrite('image_encryption/'+str(c) + '.jpg',frame)
	c = c + 1

	out.write(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
