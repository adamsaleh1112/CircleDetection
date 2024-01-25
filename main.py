import numpy # importing numpy, an array library that allows video data to be stored in arrays
import cv2 # importing opencv-python, an image processing library that allows functions such as blur, cropping, etc.

image = cv2.imread("Can.jpg") # loads image
bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converts it to grayscale

detected = cv2.HoughCircles(bw, cv2.HOUGH_GRADIENT, 1.2, 100) # detects circles

if detected is not None: # makes sure that it detected at least one

	circles = numpy.uint16(numpy.around(detected)) # converts circles to x, y, and radius parameters

	for parameter in circles[0, :]: # iterating through all circles' detected parameters
		x, y, r = parameter[0], parameter[1], parameter[2] # setting x, y, and r to the respective parameters

		# DRAWING MAIN CIRCLE
		cv2.circle(image, (x, y), r, (0, 255, 0), 7) # args: image, coordinates, radius, color, stroke

		# DRAWING MID POINT
		cv2.circle(image, (x, y), 1, (0, 0, 255), 10) # drawing a circle with a radius of 1 (dot) at same coordinates

		# WINDOW
		cv2.imshow("Detected Circle", image) # creating window called Detected Circle that displays output image
		cv2.waitKey(0)