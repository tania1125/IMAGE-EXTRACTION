import fitz
file = fitz.open('report.pdf')
#for pageNumber, page in enumerate(file.pages(), start=1):
#    for imgNumber, img in enumerate(file.get_page_images(), start=1):
image_list=file.get_page_images(1)
for image in image_list:
        xref = img[0]
        pix = fitz.Pixmap(file, xref)
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.writePNG(f'image_page{pageNumber}_{imgNumber}.png')