#调用摄像头
#导入库
import cv2

#打开摄像头
capture=cv2.VideoCapture('video1.avi')

#获取摄像头实时画面
cv2.namedWindow("video")
while True:
    #读取帧
    ret,frame = capture.read()
    #渲染画面
    cv2.imshow('Danfer',frame)
    #暂停窗口
    if cv2.waitKey(25) & 0xFF == ord('Q'):
        break

#释放资源
capture.release()

#关闭窗口
cv2.destroyAllWindows()

