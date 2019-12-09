import cv2,numpy
from databaseOperation import imageOperations

class ParseProcess:

    def parseImage(self,image):

        frameCountX=3
        frameCountY=3

        frameSizeX=61
        frameSizeY=61

        frames=[]
        counterX=0
        counterY=0

        for i in range(frameCountX):
            for j in range(frameCountY):
                cropImg = image[counterY:counterY+frameSizeY, counterX:counterX+frameSizeX]
                counterX=counterX+frameSizeX
                frames.append(cropImg)

            counterY=counterY+frameSizeY
            counterX=0

        return frames

    def getRandomImagePath(self):
        import random
        imageProces=imageOperations('database.db')
        images=imageProces.getImages()
        if(len(images)>0):
            rnd=random.randint(0,len(images)-1)
            return images[rnd][1],images[rnd][3],images[rnd][2]
        else:
            return images

    def getFrames(self):
        path=self.getRandomImagePath()
        if(len(path)>0):
            self.image=cv2.imread(path[0])
            return self.parseImage(self.image),path[1],path[2]
        else:
            return False

    def convertGray(self,frame):
        resultImage=numpy.zeros((frame.shape[0],frame.shape[1],1),dtype=numpy.uint8)
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                resultImage[i,j]=frame[i,j,0]*0.299+frame[i,j,1]*0.587+frame[i,j,2]*0.114
        return resultImage

    def saveClickedFrames(self,frames):
        counter=1
        for frame in frames:
            frame=self.convertGray(frame)
            cv2.imwrite('frames/bf'+(str)(counter)+'.png',frame)
            counter=counter+1
