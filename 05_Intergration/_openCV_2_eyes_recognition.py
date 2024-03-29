# 얼굴 인식 프로그램

import cv2
import sys, os

if not os.path.exists("./pakutas"):
    os.mkdir("./pakutas")

# 입력 파일 지정하기
#image_file = "./pakutas/photo1.jpg"
image_file = "./pakutas/photo2.jpg"

# 캐스케이드 파일의 경로 지정하기
cascade_file = "./cascades/data/haarcascade_eye.xml"
# 이미지 읽어 들이기
image = cv2.imread(image_file)

# 그레이스케일로 변환하기
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 특징 파일 읽어 들이기
cascade = cv2.CascadeClassifier(cascade_file)

# 얼굴 인식 실행하기
face_list = cascade.detectMultiScale(image_gs,
            scaleFactor=1.3,
            minNeighbors=1,
            minSize=(30,30))
# scaleFactor - 이미지 스케일
# minNeighbors - 얼굴 검출 후보들의 갯수
# minSize - 가능한 최소 객체 사이즈
if len(face_list) > 0:
    # 인식한 부분 표시하기
    print(face_list)
    color = (0,0,255)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h),color,thickness=8)

    # 파일로 출력하기
    cv2.imwrite("facedetect-output2.PNG",image)
else:
    print("no face")