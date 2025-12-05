import fitz

doc = fitz.open("sample2.pdf")
with open("links.txt",'a') as txt:
    for page in doc:
        links = page.get_links()
        for link in links:
            if link['kind'] == 2:
                if link.get('uri'):
                    txt.write(link.get('uri') + '\n')