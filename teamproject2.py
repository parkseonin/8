import cv2
import numpy as np

imgfile = 'C:/Users/User/miniconda3/Lib/site-packages/cv2/team11/one.jpg'
imgfile1 = 'C:/Users/User/miniconda3/Lib/site-packages/cv2/team11/mask_off.jpg'

# cascade 호출
#cascade_file = "C:/Users/User/miniconda3/Lib/site-packages/cv2/team11/haarcascade_frontface_default.xml"
cascade_file = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#cascade_file1 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread(imgfile)
#image1 = cv2.imread(imgfile1)
#cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade_file.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10), maxSize = (1000, 1000))
#face_list1 = cascade_file1.detectMultiScale(image1, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10), maxSize = (1000, 1000))

y1, x1, z1 = np.shape(image)

if len(face_list) > 0:    
  color = (0, 0, 255)
  for face in face_list:
    x, y, w, h = face
    # 얼굴 면적 계산
    percent = round((w * h) / (x1 * y1) * 100, 0)
    if mask >= percent * 0.5:
        print("마스크를 씀")
    else:
        print("마스크를 안씀")
    # 면적에 따른 색 지정
    if percent >= 30:
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)
    # 사각형
    cv2.rectangle(image,(x,y),(x+w,y+h),color,10)
    # 텍스트
    cv2.putText(image, str(percent) + '%', (x, y), cv2.FONT_HERSHEY_PLAIN, int(8), color, int(8), 1)
  # 저장
  cv2.imwrite("C:/Users/User/miniconda3/Lib/site-packages/cv2/team11/one.jpg", image)

else:
  print("none")