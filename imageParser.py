import cv2

class ParseProcess:

    def __init__(self,FrameCount,GetImageCount,FileName):
        self.frameCount=FrameCount
        self.fileName=FileName
        self.getImageCount=GetImageCount
        self.image=FileName #sahte ilk atama

    def parseImage(self,image):

        frameCountX=(int)((self.frameCount)**0.5)
        frameCountY=(int)((self.frameCount)**0.5)

        frameSizeX=(int)(image.shape[0]/frameCountX)
        frameSizeY=(int)(image.shape[1]/frameCountY)

        print("Frame Count: ",frameCountX,"X",frameCountY) #istenilen frameCount miktarına göre oluşacak olan yeni captcha miktarını yazar
        print("Frame Size: ",frameSizeX,"X",frameSizeY) #istenilen frameCount miktarına göre oluşacak olan herbir karenin ebatını yazar

        frames=[]
        counterX=0
        counterY=0

        for i in range(frameCountX):
            for j in range(frameCountY):
                cropImg = image[counterY:counterY+frameSizeY, counterX:counterX+frameSizeX]
                counterX=counterX+frameSizeX
                frames.append(cropImg)
                #cv2.imshow("crpImg"+(str)(len(frames)),cropImg)  #oluşan her bir frameyi gösterme

            counterY=counterY+frameSizeY
            counterX=0
            

        return frames



    def getFrames(self,GetImageCount):
        self.getImageCount=self.getImageCount+1
        self.image=cv2.imread(self.fileName)
        self.getImageCount=GetImageCount
        if(GetImageCount==0):
            return self.parseImage(self.image)
        else:
            self.frameCount=(self.frameCount**0.5+1)**2
            return self.parseImage(self.image)
        #cv2.imshow("Image Count : "+(str)(self.getImageCount),self.image) #genel resmi göstertme
        #cv2.waitKey(0)