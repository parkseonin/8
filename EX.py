# 오픈소스 과제
# 인식된 사람 수 반환
# 사진에서 하얀색(마스크-크기도) 검출
# 기준 정해서 마스크 낀 걸로 인식

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('./one.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),2)
    face_gray=gray[y: y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]
        
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()