import fitz

doc = fitz.open("sample.pdf")

count = 1
for page in doc:

    if count == 5:
        page.set_rotation(90)
    count += 1
doc.save("new.pdf")

doc.close()