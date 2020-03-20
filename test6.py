'''
this script should run without memory errors and freezing up  OSD by using o.update by not keep calling add_overlay
it uses an outside module to generate image, this is done so its easier to test image generation on any platform that doesnt have picamera, etc
'''
#import generate_image #use a single string
import generate_image_lines #use list of strings

import picamera
from PIL import Image, ImageDraw
 
from time import sleep
import random


osd_image_file = generate_image_lines.image_name

#use RGBA to make transparent background, use RGB for solid background
color_style = 'RGBA'

count = 0
#data_sample = 'hellow\r\nworld\r\nthe\nquick\n'
data_sample = ['Movement Direction: Forward',
               'Speed: {}'.format(random.randint(0,10)),
               'Incline: X{} Y{} Z{}'.format(random.randint(-5,5),random.randint(-3,3),random.randint(-2,2)),
               'Battery: {}%'.format(100-count/10),
               'signal strength: 10',

               'Copyright Terrafirma Technologies 2019',
                ]
           
def create_image(text = []):
    #generate_image.create_image_with_text(text)
    generate_image_lines.create_image_with_text(text)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()

    create_image(data_sample)
    # Load the arbitrarily sized image
    img = Image.open(osd_image_file)
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new(color_style, (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)

    # Wait indefinitely until the user terminates the script
    count = 0
    while True:
        data_sample = ['Movement Direction: Forward',
                    'Speed: {}'.format(random.randint(0,10)),
                    'Incline: X{} Y{} Z{}'.format(random.randint(-5,5),random.randint(-3,3),random.randint(-2,2)),
                    'Battery: {}%'.format(100-count/10),
                    'signal strength: 10',

                    'Copyright Terrafirma Technologies 2019',
                        ]
        create_image(data_sample)
        count +=1
        # Load the arbitrarily sized image
        img = Image.open(osd_image_file)

        # Create an image padded to the required size with
        # mode 'RGB'
        pad = Image.new(color_style, (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
            ))
        # Paste the original image into the padded one
        pad.paste(img, (0, 0))

        # By default, the overlay is in layer 0, beneath the
        # preview (which defaults to layer 2). Here we make
        # the new overlay semi-transparent, then move it above
        # the preview
        o.alpha = 0
        o.layer = 3
        sleep(1)
        o.update(pad.tostring())
        #camera.remove_overlay(o)
