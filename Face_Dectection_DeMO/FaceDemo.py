# #识别图片
# #导入库
# import cv2
#
# #加载图片
# image = cv2.imread('F:\exp-study\TengfeibeiTiaozhanbei\DeMO\image1.jpg')
#
# #创建窗口
# cv2.namedWindow('window')
#
# #显示图片
# cv2.imshow('Danfer',image)
#
# #暂停窗口
# cv2.waitKey(0)
#
# #关闭窗口
# cv2.destroyAllWindows()


# #添加人脸识别：重点添加模型
# # #导入库
# # import cv2
# #
# # #加载照片
# # image = cv2.imread('F:\exp-study\TengfeibeiTiaozhanbei\DeMO\image1.jpg')
# #
# # #加载人脸模型
# # face = cv2.CascadeClassifier("F:\exp-study\TengfeibeiTiaozhanbei\DeMO\haarcascade_frontalface_alt.xml")
# #
# # #调整图片灰度：提高性能
# # gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# #
# # #检查人脸
# # faces = face.detectMultiScale(gray)
# #
# # #标记人脸
# # for (x,y,w,h) in faces:
# #     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
# #     #创建窗口
# #     cv2.namedWindow('window')
# #     #显示图片
# #     cv2.imshow('Danfer', image)
# # #暂停窗口
# # cv2.waitKey(0)
# # #关闭窗口
# # cv2.destroyAllWindows()


# #调用摄像头
# #导入库
# import cv2
#
# #打开摄像头
# capture = cv2.VideoCapture(0)
#
# #获取摄像头实时画面
# cv2.namedWindow("video")
# while True:
#     #读取帧
#     ret,frame = capture.read()
#     #渲染画面
#     cv2.imshow('Danfer',frame)
#     #暂停窗口
#     if cv2.waitKey(5) & 0xFF == ord('Q'):
#         break
#
# #释放资源
# capture.release()
#
# #关闭窗口
# cv2.destroyAllWindows()


# #摄像头识别人脸
# #导入库
# import cv2
#
# #加载人脸模型
# face = cv2.CascadeClassifier('F:\exp-study\TengfeibeiTiaozhanbei\DeMO\haarcascade_frontalface_alt.xml')
#
# #打开摄像头
# capture = cv2.VideoCapture(0)
#
# #创建窗口
# cv2.namedWindow('video')
#
# #获取摄像头实时画面
# while True:
#     #读取帧
#     ret,frame = capture.read()
#     #调整灰度
#     gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
#     #检查人脸
#     faces = face.detectMultiScale(gray)
#     #标记人脸
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#     #显示图片
#     cv2.imshow('video',frame)
#     #暂停窗口
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
# #释放资源
# capture.release()
# #关闭窗口
# cv2.destroyAllWindows()
