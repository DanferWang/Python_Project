#导入库
import cv2

#加载人脸模型
face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#打开摄像头
capture = cv2.VideoCapture(0)

#获取摄像头实时画面
while True:
    #读取帧
    ret,frame = capture.read()
    #调整灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #检查人脸
    faces = face.detectMultiScale(gray)
    #标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #显示图片
    cv2.imshow('Camera(press Q to exit)',frame)
    #暂停窗口
    if cv2.waitKey(25) & 0xFF == ord('Q'):
        break
#释放资源
capture.release()
#关闭窗口
cv2.destroyAllWindows()