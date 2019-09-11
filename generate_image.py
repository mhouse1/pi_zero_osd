'''
usage
'''
from PIL import Image, ImageDraw, ImageFont
import random
import os

image_name = 'osd_text.png'
font_location = os.path.join(os.path.dirname(os.path.realpath(__file__)),'Arial.ttf')
def create_image_with_text(text):
    image_width = 1000
    image_height = 500
    img = Image.new('RGBA', (image_width, image_height), color = (255,255, 255,0))
    #fnt = ImageFont.truetype(font_location, 30)
    d = ImageDraw.Draw(img)
    push_text_right = 0
    #d.text((push_text_right,200), text,font = fnt, fill=(255,0,0))
    d.text((push_text_right,200), text, fill=(255,0,0))

    
    
    img.save(image_name,'PNG')


if __name__ == '__main__':
    #create_image_with_text('hello world asdjfklasjdfalsjfal \n asdjfaosdfjasopdfjasdofajsd \n ajiofajsofjasdof \n apdofjasdofjasdofjads \n adifajhsidofjaosdj f\n')

    #simulate crawler osd data
    print("using font location",font_location)
    count = 50
    data_sample = '\
    Movement Direction: {}\n\
    Speed:{} feet per minute\n\
    Incline: X{}, Y{}, Z{}\n\
    battery level: {}\n\n\
    Copyright Terrafirma Technologies 2019'\
                        .format('forward',random.randint(0,10),
                                random.randint(-5,5),random.randint(-3,3),random.randint(-2,2),
                                100-count/10)
    create_image_with_text(data_sample)