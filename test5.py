'''
I believe this script can run without freezing up due to memory issues

it creates a image and overlays on top of video
'''

import picamera
from PIL import Image, ImageDraw
 
from time import sleep


def create_image(text = 'none'):
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    
    d = ImageDraw.Draw(img)
    d.text((10,10), text, fill=(255,255,0))
    
    img.save('myosd.png')

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()

    create_image('hello world\n see you soon')
    # Load the arbitrarily sized image
    img = Image.open('myosd.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)

    # Wait indefinitely until the user terminates the script
    toggle = False
    count = 0
    while True:
        create_image('hello world'+str(count))
        count +=1
        # Load the arbitrarily sized image
        img = Image.open('myosd.png')

        # Create an image padded to the required size with
        # mode 'RGB'
        pad = Image.new('RGB', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
            ))
        # Paste the original image into the padded one
        pad.paste(img, (0, 0))

        # By default, the overlay is in layer 0, beneath the
        # preview (which defaults to layer 2). Here we make
        # the new overlay semi-transparent, then move it above
        # the preview
        o.alpha = 30
        o.layer = 3
        sleep(1)
        o.update(pad.tostring())
        #camera.remove_overlay(o)
