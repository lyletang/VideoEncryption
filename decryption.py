import cv2

videoCapture = cv2.VideoCapture('encryption.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

#v = cv2.VideoWriter('bb.mp4', cv2.cv.CV_FOURCC('M','J','P','G'), fps, size)
v = cv2.VideoWriter('decryption.avi',cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)

print fps, size, 'v->', v

success, frame = videoCapture.read()

tmp = 1

while success:
	filePath = 'image_decryption/' + str(tmp) + '.jpg'
	img = cv2.imread(filePath)
	#cv2.imshow('mywindow',frame)
	tmp = tmp + 1
	cv2.waitKey(1000/int(fps))
	v.write(img)
	success, frame = videoCapture.read()
