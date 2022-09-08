import cv2
import numpy as np

def save_image(image,addr,num):
    addrress=addr+str(num)+'.jpg'
    cv2.imwrite(addrress,image)

video=cv2.VideoCapture('./BadApple.mp4')
success,frame=video.read()
i=0
timeF=1
j=0
while success:
    i=i+1
    if(i%timeF==0):
        j=j+1
        save_image(frame,'./Bad/',j)
        print('save image:',j)
    success,frame=video.read()