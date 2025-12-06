import fitz

doc = fitz.open(r"C:\Users\Ajay kumar\Downloads\PDF Processor Project\sample.pdf")

doc.set_metadata({
    "title": "My PDF",
    "author": "Omkar"
})


doc.save('meta_edited.pdf')


doc1 = fitz.open('meta_edited.pdf')
print(doc1.metadata)
doc.close()