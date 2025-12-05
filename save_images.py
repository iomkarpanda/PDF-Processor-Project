import fitz

doc = fitz.open("sample2.pdf")
count = 1
for page in doc:
    images = page.get_images()
    for image in images:
        xref = image[0]
        pix = fitz.Pixmap(doc,xref)

        if pix.alpha:
            pix = fitz.Pixmap(fitz.csRGB, pix)
            
        pix.save(f'{count}.png')
        count += 1
