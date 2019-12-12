import sys
import os
mode=sys.argv[1]
img_ext=sys.argv[2].split('.')[1]
if mode=="-d":
    msg=''
    byte_msg=[]
    img=open(sys.argv[2],"rb").read()
    byte_img=bytearray(img)
    Eof={'jpg':0xD9, 'png':0x44}
    for byte in byte_img[::-1]:
        if byte==Eof[img_ext]:
             break
        byte_msg.append(byte)
    for letter in byte_msg[::-1]:
        msg+=str(chr(letter))
    print(msg)    
elif mode=="-e":
    img=open(sys.argv[2],"ab")
    msg=input("Enter a message to hide-> ")
    img.write(msg.encode('utf-8'))
                
        
