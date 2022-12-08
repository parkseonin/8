import cv2
import numpy as np

imgfile = 'C:/Users/LG/image/face.jpg'

# cascade 호출
#cascade_file = "C:/Users/LG/haarcascade_frontface_default.xml"

cascade_file = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread(imgfile)
#cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade_file.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10), maxSize = (1000, 1000))

y1, x1, z1 = np.shape(image)

if len(face_list) > 0:
  color = (0, 0, 255)
  for face in face_list:
    x, y, w, h = face
    # 얼굴 면적 계산
    percent = round((w * h) / (x1 * y1) * 100, 0)
    # 면적에 따른 색 지정
    if percent >= 30:
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)
    # 사각형
    cv2.rectangle(image,(x,y),(x+w,y+h),color,5)
    # 텍스트
    cv2.putText(image, str(percent) + '%', (x, y), cv2.FONT_HERSHEY_PLAIN, int(3), color, int(3), 2)
    # 마스크 부분 검출
    cv2.rectangle(image, (x,(2*y+h)/2),(x+w,x+h),(0,255,0),3)

else:
  print("none")

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()