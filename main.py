# STEP 1
# import libraries
import fitz
fitz.restore_aliases()
import io
from PIL import Image
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGul as qtg
from PyQt5 import QtCore as qtc

# STEP 2
# file path you want to extract images from
file = "C:/Users/ashbi/Desktop/project/report.pdf"

# open the file

pdf_file= fitz.open(file)
# enter the page number where ur desired image is
n=int(input("enter the page number"))
page= pdf_file[n]
image_list = page.get_images()
ln=len(image_list)
#we get the number of images in that page
if image_list:
    		print(f"Number of images= {ln}")
else:
		print(" No images found on page")
#To see those images and save from those	