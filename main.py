# STEP 1
# import libraries
import fitz
fitz.restore_aliases()
import io
from PIL import Image


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
for image in image_list:
      xref=image[0]
      pix=fitz.Pixmap(pdf_file,xref)
      #if pix.n<5:
           # pix.save(f'{xref}.jpg')#
      if not pix.colorspace.name in (fitz.csGRAY.name, fitz.csRGB.name):
        pix = fitz.Pixmap(fitz.csRGB, pix)
      else:
            pix1=fitz.open(fitz.csRGB,pix)
            print(pix1)
            pix1.save(f'{ln}.png')
            #pix1.save(f'{image_list}.png')
            pix1=None
      pix=None
print(len(image_list),'detected')