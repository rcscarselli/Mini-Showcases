from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#defining the parameters for RGB here
	b = frame[:, :, :1]
	g = frame[:, :, 1:2]
	r = frame[:, :, 2:]

#grabbing the average of the found values from above to present the majority color
	b_mean = np.mean(b)
	g_mean = np.mean(g)
	r_mean = np.mean(r)

	if (b_mean > g_mean and b_mean > r_mean):
		print("Blue")
	if (g_mean > r_mean and g_mean > b_mean):
		print("Green")
	else:
		print("Red")

cap.release()
cv2.destroyAllWindows()