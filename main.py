#!/usr/bin/python
'''
date:9/8/2019
author: Michael House
'''
import picamera
import time
import numpy as np
import string
import random
import os
from datetime import datetime
import random

from PIL import Image, ImageDraw, ImageFont

# Video Resolution for recording
#set to 940 will show raspberry pi logo/status with video not taking up full screen
VIDEO_HEIGHT = 720
VIDEO_WIDTH = 1280

baseDir='/home/pi/osd/' # directory where the video will be recorded
 
os.system('clear') # clear the terminal from any other text

# Create empty images to store text overlays
canvas_width = 704
canvas_height = 120
font_size = 25
row_1 = 0
row_2 = font_size*2
row_3 = 30

textOverlayCanvas = Image.new("RGB", (canvas_width, canvas_height))
textOverlayPixels = textOverlayCanvas.load()

# Use Roboto font (must be downloaded first)
font = ImageFont.truetype("/home/pi_zero_osd/Roboto-Regular.ttf", font_size) 

def run_osd():
   '''
   runs pi camera with overlay text. 
   

   Note: i still am not able to solve the memory issue where it never frees any memory and eventually runs until it crashes
   '''
   with picamera.PiCamera() as camera:

      camera.resolution = (VIDEO_WIDTH, VIDEO_HEIGHT)
      camera.framerate = 60
      camera.led = False
      camera.start_preview()

      topText = "Alt: 310m       Spd: 45km/h         Dir: N"
      bottomText = "TerrafirmaTechnology.com   "

      topOverlayImage = textOverlayCanvas.copy()
      bottomOverlayImage = textOverlayCanvas.copy()

      # Load the crosshair image
      crosshairImg = Image.open('crosshair.png')

      # Create an image padded to the required size with
      crosshairPad = Image.new('RGB', (((crosshairImg.size[0] + 31) // 32) * 100, ((crosshairImg.size[1] + 15) // 16) * 16))
      crosshairPad.paste(crosshairImg, (0,0))

      # Attach overlays 

      topOverlay = camera.add_overlay(topOverlayImage.tostring(), format='rgb', size=(canvas_width,canvas_height), layer=3, alpha=128, fullscreen=False, window=(0,20,canvas_width, canvas_height))

      bottomOverlay = camera.add_overlay(bottomOverlayImage.tostring(), format='rgb', size=(canvas_width,canvas_height), layer=4, alpha=128, fullscreen=False, window=(0,VIDEO_HEIGHT-canvas_height*2,canvas_width,canvas_height))


      count = 0


      drawTopOverlay = ImageDraw.Draw(topOverlayImage)
      drawBottomOverlay = ImageDraw.Draw(bottomOverlayImage)

      try:
         
         while True:
            #window multiply by 2 would double the size of text and canvas
            #topOverlay = camera.add_overlay(topOverlayImage.tostring(), format='rgb', size=(canvas_width,canvas_height), layer=3, alpha=128, fullscreen=False, window=(0,20,canvas_width, canvas_height))
            #bottomOverlay = camera.add_overlay(bottomOverlayImage.tostring(), format='rgb', size=(canvas_width,canvas_height), layer=4, alpha=128, fullscreen=False, window=(0,VIDEO_HEIGHT-canvas_height*2,canvas_width,canvas_height))
            #crosshairOverlay = camera.add_overlay(crosshairPad.tostring(), format='rgb', size=(canvas_width,512), layer=5, alpha=100, fullscreen=False, window=(20,20,canvas_width,512))
            #topOverlayImage = textOverlayCanvas.copy()
            #bottomOverlayImage = textOverlayCanvas.copy()


            drawTopOverlay.text((200, row_1), 'Rotations: L1: {} L2: {} R1: {} R2: {}'.format(count,count,count,count), font=font, fill=(255, 0, 255))
            x = random.randint(-5,5)
            y = random.randint(7,9)
            z = random.randint(5,6)
            drawTopOverlay.text((200, row_2), 'Distance: {} Accelerometer: X{}, Y{} Z{}'.format(count+3,x,y,z), font=font, fill=(255, 0, 255))
            topOverlay.update(topOverlayImage.tostring())

            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            drawBottomOverlay.text((20, row_1 ), bottomText+dt_string, font=font, fill=(255, 0, 0))
            drawBottomOverlay.text((20, row_2), 'Copyright Terrafirma Technologies 2019', font=font, fill=(255, 0, 0))
            bottomOverlay.update(bottomOverlayImage.tostring())
               
               #extra = camera.add_overlay(topOverlayImage.tostring(), format = 'rgb', size=(704,60), layer=3, alpha=128, fullscreen=False, window=(0,20,704,60))
               #camera.remove_overlay(extra)

            time.sleep(1)

            #camera.remove_overlay(crosshairOverlay)

            count+=1
            if count == 1000:
                  count = 0
      except KeyboardInterrupt:
         #camera.remove_overlay(topOverlay)
         #camera.remove_overlay(bottomOverlay)
         #camera.remove_overlay(crosshairOverlay)

         print "Cancelled"

      finally:
         camera.remove_overlay(topOverlay)
         camera.remove_overlay(bottomOverlay)
         #camera.remove_overlay(crosshairOverlay)


if __name__ == '__main__':
   i =  0
   while True:
      run_osd()
