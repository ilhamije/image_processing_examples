import cv2
# cap = cv2.VideoCapture('path of video file')
cap = cv2.VideoCapture('/home/ilham/Videos/test.mp4')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name',frame)
    cv2.imwrite("results/frame%d.jpg" % count, frame)
    count = count + 1
    if count == 30:
        break
    
cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows