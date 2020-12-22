import cv2
import numpy as np

iitbhu = cv2.imread('IIT-bhu-1.jpg')



iitbhu = cv2.resize(iitbhu,(800,600))




cv2.imwrite('iitbhu.jpg',iitbhu)
##cv2.imwrite('EC202.jpg',ec202)
##cv2.imwrite('E0201.jpg',eo201)
##cv2.imwrite('MO201.jpg',mo201)
##cv2.imwrite('MA202.jpg',ma202)
##cv2.imwrite('H104.jpg',h104)



