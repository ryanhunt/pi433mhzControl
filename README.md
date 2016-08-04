# pi433mhzControl
Code to control a 433mhz frequency remote from a Raspberry PI, using [IFTTT](http://www.ifttt.com/) 'Do' app. 

# Setup

Make sure you add a `secret.php` to the same folder as the `index.php`, and include the following:

    <?php
    
    $secret = '';
    $home_lat = '';
    $home_long = '';
    $openCommand = 'sudo <path-to-this-code>/pi433mhzControl/script/openDoor.py';
    
    ?>

Make sure you grant sudo access to the Apache/Web host user to the script above. On Raspbian this is usually `www-data`. Do this with `visudo` command. 

I have my setup as such:

1. Create 'Do' recipe in [IFTTT](http://www.ifttt.com/). 
2. Setup DNS redirect to my home IP.  (I'm using OpenWRT to update my DNS with a DynDNS provider)
3. Add this DNS entry to IFTTT 'do' recipe as the URL. 
4. Configure it to be 'POST' 
5. Content type = `application/x-www-form-urlencoded`
6. Body = `secret=SEKRETHASH&long={{Longitude}}&lat={{Latitude}}`

# Hardware

I followed the steps described [here](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins) to configure my Pi to control a LED. This way the code will turn the LED off if it's on, and on if it's off. Considering my Garage door will not have a sensor (for now) once I wire up the transponder, it'll simply fire off a 'open/close' command without any knowledge of it's open or closed. 

I used this hardware from [AliExpress](http://www.aliexpress.com/item/1set-RF-module-433-Mhz-superheterodyne-receiver-and-transmitter-Support-ASK-OOK-small-size-low-power/32571703475.html?spm=2114.13010608.0.71.eSqJFs).





