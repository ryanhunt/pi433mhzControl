# pi433mhzControl
Code to control a 433mhz frequency remote from a Raspberry PI, using IFTTT 'Do' app. 

Make sure you add a 'secret.php' to the same folder as the index.php, and include the following variables:

$secret = '';
$home_lat = '';
$home_long = '';
$openCommand = 'sudo <path-to-this-code>/pi433mhzControl/script/openDoor.py';

Also make sure you grant sudo access to the Apache/Web host user to the script above. On Raspbian this is www-data. Do this with 'visudo' 

I have my setup as such:

1. Create 'Do' recipe in IFTTT. 
2. Setup DNS redirect to my home IP.  (I'm using OpenWRT to update my DNS with a DynDNS provider)
3. Add this DNS entry to IFTTT user. 
4. Configure it to be 'POST' 
5. Content type = 'application/x-www-form-urlencoded'
6. Body = "secret=SEKRETHASH&long={{Longitude}}&lat={{Latitude}}





