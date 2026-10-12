import pypdf as pf
reader =pf.PdfReader("C:/Users/mdfai/Downloads/sample.pdf")
print(len(reader.pages))
page = reader.pages[0]
print(page.extract_text())

writer = pf.PdfWriter()
writer.add_blank_page(width=300,height=400)
with open("new.pdf",'wb') as file:
    writer.write(file)

