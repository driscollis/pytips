from PIL import Image

def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)


if __name__ == '__main__':
    img = 'lighthouse.jpg'
    watermark_with_transparency(img, 'lighthouse_watermarked3.jpg',
                                'watermark.png', position=(0,0))