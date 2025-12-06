import fitz

doc = fitz.open(r"C:\Users\Ajay kumar\Downloads\PDF Processor Project\sample.pdf")

page = doc[0]

#poor quality
pix = page.get_pixmap()
pix.save('first.png')

#high quality

zoom = 4
mat = fitz.Matrix(zoom, zoom)

pix1 = page.get_pixmap(matrix=mat)
pix1.save("page_high.png")