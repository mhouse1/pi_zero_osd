#Initial Pi Zero overlay + recording code

import picamera
import time
import numpy
from PIL import Image, ImageDraw, ImageFont

#enable recording
#note: does not record overlay
enabled_recording = True
enabled_overlay = False

# Video Resolution
VIDEO_HEIGHT = 720
VIDEO_WIDTH = 1280

# Cross Hair Image
crossHair = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT))
crossHairPixels = crossHair.load()
for x in range (0, VIDEO_WIDTH):
    crossHairPixels[x, 360] = (255, 255, 0)

for x in range(0, VIDEO_HEIGHT):
    crossHairPixels[640, x] = (255, 0, 0)

with picamera.PiCamera() as camera:
    camera.resolution = (VIDEO_WIDTH, VIDEO_HEIGHT)
    camera.framerate = 30
    camera.led = False
    camera.start_preview()

    if enabled_recording:
        camera.start_recording('timestamped.h264')
    img = crossHair.copy()

    #where alpha = 0 (most transparent) and 255 not transparent
    #valid alpha value is 0 to 255
    if enabled_overlay:
        overlay = camera.add_overlay(img.tostring(), layer = 3, alpha = 150) 

    time.sleep(1)
    try:
        while True:
            if enabled_overlay:
                text = time.strftime('%H:%M:%S', time.gmtime())
                img = crossHair.copy()
                draw = ImageDraw.Draw(img)
                draw.font = ImageFont.truetype("/home/pi_zero_osd/Roboto-Regular.ttf", 20)#("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 20)
                draw.text((10, 10), text, (255, 255, 255))
                draw.text((10, 100), text, (0, 255, 255))
                draw.text((10, 200), text, (255, 0, 255))
                draw.text((10, 300), text, (255, 255, 0))
                draw.text((200, 10), text, (255, 255, 255))
                draw.text((300, 100), text, (0, 255, 255))
                draw.text((400, 200), text, (255, 0, 255))
                draw.text((500, 300), text, (255, 255, 0))
                overlay.update(img.tostring())
            if enabled_recording:
                camera.wait_recording(0.9)

    finally:
        if enabled_overlay:
            camera.remove_overlay(overlay)
        if enabled_recording:
            camera.stop_recording()
