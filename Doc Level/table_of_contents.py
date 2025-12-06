import fitz

doc1 = fitz.open(r"C:\Users\Ajay kumar\Downloads\PDF Processor Project\sample.pdf")
doc2 = fitz.open(r"C:\Users\Ajay kumar\Downloads\PDF Processor Project\sample2.pdf")

toc1 = doc1.get_toc()
toc2 = doc2.get_toc()

print(toc1)
print(toc2)