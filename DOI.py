import cv2

image = cv2.imread('./image/para.jpg')
eye_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_list = eye_cascade.detectMultiScale(image, scaleFactor=1.11, minNeighbors=4, minSize=(50, 50), maxSize = (60, 60))

if len(face_list) > 0:    
  color = (0, 0, 0)
  for face in face_list:
    x, y, w, h = face
    # 사각형 그리기
    cv2.rectangle(image,(int(x-10),int(y-5)),(int(x+10)+w,y+int(h/28*14)),color,-5)

else:
  print("none") 

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()