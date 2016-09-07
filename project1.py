#project1.py
#Joshua Ryan Cruz
#CST 205 Project 1

print("hello there")


from PIL import Image
import statistics

#initializing image variables and loads images into memory;
im1 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/1.png")
im1.load()
im2 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/2.png")
im2.load()
im3 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/3.png")
im3.load()
im4 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/4.png")
im4.load()
im5 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/5.png")
im5.load()
im6 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/6.png")
im6.load()
im7 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/7.png")
im7.load()
im8 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/8.png")
im8.load()
im9 = Image.open("C:/Users/Ryan Cruz/Documents/CSIS/CST 338/CST205Project1/Project1Images/9.png")
im9.load() 

#array of all images 
images = [im1,im2,im3,im4,im5,im6,im7,im8,im9]

#create new image for median image data;
outImage = Image.new("RGB",(im1.width, im1.height))

#to iterate throught the 2d array x values
for x in range (0, im1.width):
        #to iterate throught the 2d array y values
        for y in range (0, im1.height):
                #list for pixels to be sorted within loop.
                pixelList = []
                for image in images:
                        pixelList.append(image.getpixel((x,y)))
                print("working on it")
                pixelList.sort()
                medianPixel = pixelList[4]
                outImage.putpixel((x,y),medianPixel)
                #print("working on it...")
                
outImage.show()
                



