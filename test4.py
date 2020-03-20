'''
I believe this script can run without freezing up due to memory issues
'''

import picamera
from PIL import Image
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()

    # Load the arbitrarily sized image
    img = Image.open('crosshair.png')
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
    while True:

        # Load the arbitrarily sized image
        if toggle:
            img = Image.open('crosshair.png')
        else:
             img = Image.open('crosshair1.png')
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
        o.layer = 1
        sleep(1)
        o.update(pad.tostring())
        #camera.remove_overlay(o)
