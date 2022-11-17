# Creating a Word document

import docx

my_doc = docx.Document()
my_doc.add_paragraph("Welcome to Word using Python!")
my_doc.save("test.docx")