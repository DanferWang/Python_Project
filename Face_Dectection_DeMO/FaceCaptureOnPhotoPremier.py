#导入库
import cv2

#加载照片
img = input("copy your photo to the aim directory, then input the filename of the photo which you wanna recognize:")
image = cv2.imread(img)

#加载人脸模型
face = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#调整图片灰度：提高性能
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

#检查人脸
faces = face.detectMultiScale(gray)

#标记人脸
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    #显示图片
    cv2.imshow('Danfer', image)
#暂停窗口
cv2.waitKey(0)
#关闭窗口
cv2.destroyAllWindows()
