import csv
import cv2
from PIL import Image
import os
import glob
import statistics
import numpy as np



def calculate():
    for f1 in files:
        img_file = Image.open(f1)
         # get original image parameters...
        width, height = img_file.size
        format = img_file.format
        mode = img_file.mode

        # Make image Greyscale
        img_grey = img_file.convert('L')
        #img_grey.save('result.png')
        #img_grey.show()

        # Save Greyscale values
        value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        value = value.flatten()
        print(value)
     
              
        with open("helloooo.csv", 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(value)
              
        

        
    

    
     
    


strng = ""
for i in range(65,91):
    strng = strng + chr(i)
print(strng)


for i in range(7):
    path = r"C:\Users\Pankaj\Downloads\new\image\Dataset\A"
    path = path.replace(path[36], strng[i]) 



    img_dir = path # Enter Directory of all images 
    data_path = os.path.join(img_dir,'*g')
    files = glob.glob(data_path)
    calculate()

    



