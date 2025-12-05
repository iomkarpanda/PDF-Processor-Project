import fitz

def open_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        return doc
    except fitz.FileNotFoundError:
        print("File Not Found")
        return None

def print_metadata(doc):
    title = doc.metadata['title']
    author = doc.metadata['author']
    creation_date = doc.metadata['creationDate']


    print(title if title else "None")
    print(author if author else "None")
    print(creation_date if creation_date else "None")


def extract_text(doc):
    with open('text.txt','w',encoding="utf-8") as file:
        for page in doc:
            print(page.get_text())

def extract_images(doc):
    for page in doc:
        image = page.get_images()
        print(image)
        

def page_info(doc):
    for page in doc:
        rotation = page.rotation
        mediabox = page.mediabox
        print(rotation)
        print(mediabox)

doc = open_pdf("sample2.pdf")
# print_metadata(doc)
# extract_text(doc)
page_info(doc)
# extract_images(doc)


# print(doc.pages[5].get_images())