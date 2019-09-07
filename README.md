# pi_zero_osd

requirements:
* roboto font has to be downloaded manually
* install pillow - had to also specify no cache due to memory issues
  * pip install Pillow --no-cache-dir , to install new pillow without cache
    * had to install older pillow: pip install Pillow==2.1.0

# troubleshooting
* 'unable to determine format from source size') picamera.exc.PiCameraValueError: unable to determine format from source size
  * add the parameter format='rgb' to your add_overlay call
* picamera.exc.PiCameraMMALError: no buffers available: Resource temporarily unavailable; try again later
  * put an camera.add_overlay and camera.remove_overlay inside the while loop
* picamera.exc.PiCameraMMALError: no buffers available: Resource temporarily unavailable; try again later
  * 
