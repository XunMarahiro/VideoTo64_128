from PIL import Image
import serial
import binascii,time
def Get_One(im,x,y):
    a1=im.getpixel((y,x*8))/255
    a2=im.getpixel((y,x * 8 + 1))/255
    a3=im.getpixel((y,x * 8 + 2))/255
    a4=im.getpixel((y,x * 8 + 3))/255
    a5=im.getpixel((y,x * 8 + 4))/255
    a6=im.getpixel((y,x * 8 + 5))/255
    a7=im.getpixel((y,x * 8 + 6))/255
    a8=im.getpixel((y,x * 8 + 7))/255
    val=int(a1*1+a2*2+a3*4+a4*8+a5*16+a6*32+a7*64+a8*128)
    return val
def Get_all(im):
    data=[]
    for n in range(0,8):
        for m in range(0,128):
            data.append(Get_One(im,n,m))

    return data
def Process_Str(str):
    str=str.replace("'","")
    # str = str.replace("[", "")
    # str = str.replace("]", "")
    str = str.replace('0x', '')

    # str = str.replace(',', "")
    str = str.replace(' ', "")
    return str
ser=serial.Serial("COM3",921600)

starttime = time.time()
End=''
for i in range(1,6569):
    a="./64_128/"+str(i)+'.jpg'
    image = Image.open(a)
    image=image.convert("1")
    val=Get_all(image)
    ser.write(bytes(val))
    print(i)
    a=time.time()-starttime
    while a<(i/30):
        a=time.time()-starttime








