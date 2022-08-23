from PIL import Image


def imgs2pdf(image_files: list[str], pdf_file: str) -> None:
    img = Image.open(image_files[0]).convert("RGB")
    image_objects =[Image.open(image).convert("RGB") for image in image_files[1:]]
    img.save(pdf_file, save_all=True, append_images=image_objects)

if __name__ == "__main__":
    imgs2pdf(["buffalo.jpg", "flowers_dallas.jpg", "lighthouse.jpg"], "pictures.pdf")