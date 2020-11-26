import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('fram',frame)
    c=cv2.waitKeyEx(1)
    if c==ord('q'):
        break
cap.release()
# img=cv2.imread('../static/img/1.jpg',0)
# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.xticks([]),plt.yticks([])
# plt.show()