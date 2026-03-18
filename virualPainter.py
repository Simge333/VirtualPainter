#Note : python -m venv venv than venv\Scripts\Activate in terminal
import cv2
import numpy as np
import time #show the frame rate
import os #access the file system
import HandTrackingModule as htm

##########
brushThickness=15
eraserThickness=100
##########
folderPath="Header"
myList=os.listdir(folderPath)
print(myList)
overlayList=[]
for imPath in myList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header= overlayList[0]
drawColor=(255,0,255)

cap=cv2.VideoCapture(0)
cap.set(3,1280) #width
cap.set(4,720) #height

detector=htm.handDetector(detectionCon=0.85)
xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8) #canvas for drawing
while True:
    #1.import image
    success, img=cap.read()
    img = cv2.resize(img, (1280, 720))
    img=cv2.flip(img,1) #flip the image to get the mirror image
    
    #2.find hand landmarks
    img=detector.findHands(img)
    lmlist=detector.findPositions(img, draw=False)
    if len(lmlist)!=0:
       #  print(lmlist)

        x1,y1=lmlist[8][1:] #index finger tip
        x2,y2=lmlist[12][1:] #middle finger tip

        #3.check which fingers are up
        fingers=detector.fingersUp() #which finger is up
        print(fingers)

        # 4.if selection mode - two fingers are up 
        if fingers[1] and fingers[2]:

            xp,yp=0,0 #reset the previous points

            print("Selection Mode")
            if y1<125:
                if 250<x1<450:
                    header=overlayList[0]
                    drawColor=(255,0,255)
                elif 550<x1<750:
                    header=overlayList[1]
                    drawColor=(255,0,0)
                elif 800<x1<950:
                    header=overlayList[2]
                    drawColor=(0,255,255)
                elif 1050<x1<1200:
                    header=overlayList[3]
                    drawColor=(0,0,0)
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)
        
        #5.if drawing mode - index finger is up
        if fingers[1] and fingers[2]==False:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            print("Drawing Mode")
            if xp==0 and yp==0:
                xp,yp=x1,y1


            if drawColor==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
            else:
                cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
           
            xp,yp=x1,y1
  
       
        imgGray=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY) 
        _, imgInv=cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV) #invert the image
        imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR) #convert back to color image
        img=cv2.bitwise_and(img,imgInv) #combine the video feed and the inverted canvas
        img=cv2.bitwise_or(img,imgCanvas) #combine the video feed and the canvas
   
   #setting the image 
    header_resized = cv2.resize(header, (1280, 125))
    img[0:125, 0:1280] = header_resized
    #img =cv2.addWeighted(img,0.5,imgCanvas,0.5,0) #combine the canvas and the video feed
    cv2.imshow("Image", img)
    #cv2.imshow("Canvas", imgCanvas)
    #cv2.imshow("Inv", imgInv)
    cv2.waitKey(1)