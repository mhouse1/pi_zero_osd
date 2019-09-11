# pi_zero_osd

requirements:
* roboto font has to be downloaded manually
* install pillow - had to also specify no cache due to memory issues
  * pip install Pillow --no-cache-dir , to install new pillow without cache
    * had to install older pillow: pip install Pillow==2.1.0 to resolve error "tostring() has been removed. Please call tobytes() instead."
* python3 setup
  * sudo apt-get install python3-pip
  * sudo apt-get install libopenjp2-7
  * sudo apt install libtiff5
  * sudo apt-get install python3-picamera




# usage
* to retrieve or send files off to pi zero
 * download FileZilla username: pi password: raspberry by default
 
# development
* configure your pi with your wifi name and password, then you can ssh to it using "ssh pi@raspberrypi.local" password "raspberry" by default
* running script on bootup
 * use command "pi@raspberrypi:~ $ sudo nano /etc/rc.local
" to edit the rc.local and add the following to the end of rc.local before the exit 0

    * #rc.local is run by root rather than the pi user, so we need to switch to the pi user before running the python script
    * cd /home/pi_zero_osd #change directory to the script location, required if your code does not use relative paths
    * sudo -H -u pi python /home/pi_zero_osd/main.py &
* to terminal the python script thats loaded by rc.local, you can ssh to it and run command "killall python"


# troubleshooting
* 'unable to determine format from source size') picamera.exc.PiCameraValueError: unable to determine format from source size
  * add the parameter format='rgb' to your add_overlay call
* picamera.exc.PiCameraMMALError: no buffers available: Resource temporarily unavailable; try again later
  * this is caused by the overlay but the program works, the only solution right now is to disable the error or put an camera.add_overlay and camera.remove_overlay inside the while loop at the beginning and end, but this makes the OSD flicker every loop

  
* mmal: No data received from sensor. Check all connections, including the Sunny one on the camera board
  * in my case this was caused by a bad camera (was using black noir V2 pi camera), try swapping for a new one

