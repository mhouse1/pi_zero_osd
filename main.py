#!/usr/bin/python

import picamera
import time
import numpy as np
import string
import random
import os
import datetime

from PIL import Image, ImageDraw, ImageFont

# Video Resolution for recording
#set to 940 will show raspberry pi logo/status with video not taking up full screen
VIDEO_HEIGHT = 720
VIDEO_WIDTH = 1280

baseDir='/home/pi/osd/' # directory where the video will be recorded
 
os.system('clear') # clear the terminal from any other text

# Create empty images to store text overlays
textOverlayCanvas = Image.new("RGB", (704, 60))
textOverlayPixels = textOverlayCanvas.load()

# Use Roboto font (must be downloaded first)
font = ImageFont.truetype("/home/pi_zero_osd/Roboto-Regular.ttf", 40) 

with picamera.PiCamera() as camera:
   camera.resolution = (VIDEO_WIDTH, VIDEO_HEIGHT)
   camera.framerate = 60
   camera.led = False
   camera.start_preview()

   topText = "Alt: 310m       Spd: 45km/h         Dir: N"
   bottomText = "        TerrafirmaTechnology.com         "

   topOverlayImage = textOverlayCanvas.copy()
   bottomOverlayImage = textOverlayCanvas.copy()

   # Load the crosshair image
   crosshairImg = Image.open('crosshair.png')

   # Create an image padded to the required size with
   crosshairPad = Image.new('RGB', (((crosshairImg.size[0] + 31) // 32) * 32, ((crosshairImg.size[1] + 15) // 16) * 16))
   crosshairPad.paste(crosshairImg, (0, 0))

   # Attach overlays 
   topOverlay = camera.add_overlay(topOverlayImage.tostring(), format='rgb', size=(704,60), layer=3, alpha=128, fullscreen=False, window=(0,20,704,60))
   bottomOverlay = camera.add_overlay(bottomOverlayImage.tostring(), format='rgb', size=(704,60), layer=4, alpha=128, fullscreen=False, window=(0,500,704,60))
   crosshairOverlay = camera.add_overlay(crosshairPad.tostring(), format='rgb', size=(704,512), layer=5, alpha=10, fullscreen=False, window=(20,30,704,512))

   try:
      while True:
         topOverlayImage = textOverlayCanvas.copy()
         bottomOverlayImage = textOverlayCanvas.copy()

         drawTopOverlay = ImageDraw.Draw(topOverlayImage)
         drawTopOverlay.text((200, 15), topText, font=font, fill=(255, 0, 255))

         topOverlay.update(topOverlayImage.tostring())

         drawBottomOverlay = ImageDraw.Draw(bottomOverlayImage)
         drawBottomOverlay.text((150, 20), bottomText+str(datetime.datetime.now()), font=font, fill=(255, 0, 0))

         bottomOverlay.update(bottomOverlayImage.tostring())
         
         #extra = camera.add_overlay(topOverlayImage.tostring(), format = 'rgb', size=(704,60), layer=3, alpha=128, fullscreen=False, window=(0,20,704,60))
         #camera.remove_overlay(extra)
         time.sleep(1)

   except KeyboardInterrupt:
      camera.remove_overlay(topOverlay)
      camera.remove_overlay(bottomOverlay)
      camera.remove_overlay(crosshairOverlay)

      print "Cancelled"

   finally:
      camera.remove_overlay(topOverlay)
      camera.remove_overlay(bottomOverlay)
      camera.remove_overlay(crosshairOverlay)

