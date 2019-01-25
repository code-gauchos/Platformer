from PIL import Image

class Level():
    Index=0
    def __init__(self, name, length, height, file):
        if type(length) is not type(2) or length < 1:
            return
        self.length=length
        self.height=height
        self.tempData=Level.ParseLevel(file, length, height)
        self.data=None
        self.number=Level.Index
        Level.Index+=1

    @staticmethod
    def ParseLevel(file, Length, Height):
        result=[]

        img = Image.open("src/res/img/levels/"+file)
        width, height = img.size
        pixels=img.load()
        for i in range(width):
            for j in range(height):
                result.append(pixels[i,j])

        if width is not Length:
            raise TypeError("Length and image width do not match! "+file)
        if height is not Height:
            raise TypeError("Length and image width do not match! "+file)


        return result
