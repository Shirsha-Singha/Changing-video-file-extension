import cv2

"""This is the python script to change any video 
file to another video file while also changing the resolution"""

cap = cv2.VideoCapture("test.mp4")
print(cap.isOpened())   #will print true if video is read successfully
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("test.avi", fourcc, 20.0, (640, 360))
print(out.isOpened())  #will also print true if video is written successfully
cap.release()
out.release()