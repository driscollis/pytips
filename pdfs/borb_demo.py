from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF

def main(pdf_path):
    pdf = Document()

    # Add a blank page to the PDF
    page = Page()
    pdf.append_page(page)

    # Create a layout to hold your text
    layout = SingleColumnLayout(page)

    # Add some text using the Paragraph class
    layout.add(Paragraph("Hello from borb!"))

    with open(pdf_path, "wb") as pdf_fh:
        PDF.dumps(pdf_fh, pdf)

if __name__ == "__main__":
    main("demo.pdf")
