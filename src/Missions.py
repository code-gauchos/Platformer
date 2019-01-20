from PIL import Image

class Mission():
    Index=0
    def __init__(self, name, length, file):
        if type(length) is not type(2) or length < 1:
            return
        self.length=length
        self.tempData=Mission.ParseMission(file, length)
        self.data=None
        self.number=Mission.Index
        Mission.Index+=1

    @staticmethod
    def ParseMission(file, length):
        result=[]

        img = Image.open("src/res/img/missions/"+file)
        width, height = img.size
        pixels=img.load()
        for i in range(width):
            for j in range(height):
                result.append(pixels[i,j])
        
        if width is not length:
            raise TypeError("Length and image width do not match! "+file)

        return result