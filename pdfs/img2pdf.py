from PIL import Image


def img2pdf(image_file, pdf_file):
    img = Image.open(image_file)
    img.save(pdf_file)

if __name__ == "__main__":
    img2pdf("buffalo.jpg", "buffalo.pdf")