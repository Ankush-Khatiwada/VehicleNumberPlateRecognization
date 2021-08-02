import numpy as np 
import cv2
from PIL import Image
import pytesseract as tess 



#Function  to check the area range and width-height ratio

def ratio(area, width,height):
	ratio = float(width)/float(height)
	if ratio < 1:
		ratio = 1/ ratio
	if (area<1063.62 or area> 73862.5) or (ratio<3 or ratio> 6):
		return False
	return True

#Average of image matrix

def max_White(plates):

	avg= np.mean(plates)
	if(avg >= 115):
		return True
	else:
		return False



