from PIL import Image
import cv2
def save_image(image,addr,num):
    addrress=addr+str(num)+'.jpg'
    cv2.imwrite(addrress,image)


for i in range(1,6965):
    a="./Bad/"+str(i)+'.jpg'
    b="./64_128/"+str(i)+'.jpg'
    image = Image.open(a)
    image=image.resize((128, 64))
    image.save(b)