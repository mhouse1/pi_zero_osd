'''
usage
'''
from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap


image_name = 'osd_text.png'
font_location = os.path.join(os.path.dirname(os.path.realpath(__file__)),'Arial.ttf')


def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        #x_text = ((image_width - line_width) / 2 #centered
        x_text = 0#left align
        draw.text((x_text, y_text), line, font=font, fill=text_color)
        y_text += line_height


def create_image_with_text(text):
    image_width = 1280
    image_height = 720
    
    img = Image.new('RGBA', (image_width, image_height), color = (255,255, 255,0))
    fnt = ImageFont.truetype(font_location, 20)
    d = ImageDraw.Draw(img)
    push_text_right = 0
    #d.text((push_text_right,200), text,font = fnt, fill=(255,0,0))
    #d.text((push_text_right,200), text, fill=(255,0,0))
    text_color = (255, 0, 0)
    # text1 = 'hello world'
    # text2 = 'asdfa safasdf'
    # draw_multiple_line_text(img, text1, fnt, text_color, 0)
    # draw_multiple_line_text(img, text2, fnt, text_color, 400)

    count = 0
    for line in text:
        draw_multiple_line_text(img, line, fnt, text_color, count*100)
        count +=1

    
    img.save(image_name,'PNG')


if __name__ == '__main__':
    #create_image_with_text('hello world asdjfklasjdfalsjfal \n asdjfaosdfjasopdfjasdofajsd \n ajiofajsofjasdof \n apdofjasdofjasdofjads \n adifajhsidofjaosdj f\n')

    #simulate crawler osd data
    print("using font location",font_location)
    count = 50
    data_sample = ['asdfads',
                'asdfads',
                'asdfads',
                'asdfads',
                'asdfads',

                'asdfads',
                    ]
    create_image_with_text(data_sample)