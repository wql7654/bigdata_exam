import cv2, sys, re

# 입력 파일 지정하기
'''
if len(sys.argv) <= 1:
    print("no input file")
    quit()
image_file = sys.argv[1]
'''
#image_file = "./pakutas/photo3.jpg"
image_file = "./pakutas/RedVelvet.jpg"

# 출력 파일 이름
#output_file = re.sub(r'\,jpg|jpeg|PNG$','-mosaic.jpg',image_file)
output_file = "./mosaic_output2.jpg"
mosaic_rate = 10    # 백분율로 모자이크 픽셀 두께 지정

# 캐스캐이드 파일 경로 지정하기
cascade_file = "./cascades/data/haarcascade_frontalface_alt.xml"

# 이미지 읽어 들이기
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이스케일 변환

# cascade - 폭포처럼 떨어지는, 작은 폭포, 직렬로 하다, 직렬(축전기의)

# 얼굴 인식 실행하기
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(image_gs,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(80,80))
# scaleFactor - 이미지 스케일
# minNeighbors - 얼굴 검출 후보들의 갯수
# minSize - 가능한 최소 객체 사이즈
if len(face_list) == 0:
    print("no face")
    quit()
    
# 확인한 부분에 모자이크 거기
print(face_list)
color = (0,0,255)

for(x,y,w,h) in face_list:
    # 얼굴 부분 자르기
    face_img = image[y:y+h, x:x+w]
    # 자른 이미지를 지정한 배율로 확대/축소하기
    face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
    # 확대/축소한 그림을 원래 크기로 돌리기
    face_img = cv2.resize(face_img, (w,h),
        interpolation=cv2.INTER_AREA)
    # 원래 이밎에 붙이기
    image[y:y+h,x:x+w] = face_img

# 렌더링 결과를 파일에 출력
cv2.imwrite(output_file,image)