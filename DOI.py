import cv2

imgfile = './image/para.jpg'
cascade_file = "haarcascade_frontalface_default.xml"

image = cv2.imread(imgfile)
cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade.detectMultiScale(image, scaleFactor=1.14, minNeighbors=2, minSize=(50, 50), maxSize = (60, 60))

if len(face_list) > 0:    
  color = (0, 247, 230)
  for face in face_list:
    x, y, w, h = face
    # 사각형 그리기
    cv2.rectangle(image,(x,y+int(h/28*10)),(x+w,y+int(h/28*14)),color,-5)

else:
  print("none") 

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()