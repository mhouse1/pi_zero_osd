import picamera
import datetime as dt
import time

print 'starting camera  v1'
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()

    #set background for text to black
    #camera.annotate_background = picamera.Color(0,0,0)

    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S testing \n hello world')
    #camera.start_recording('timestamped.h264')
    start = dt.datetime.now()
    #while (dt.datetime.now() - start).seconds < 30:#run for 30 seconds
    while True:#run forever
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #camera.wait_recording(0.2)
        time.sleep(1)
    #camera.stop_recording()
