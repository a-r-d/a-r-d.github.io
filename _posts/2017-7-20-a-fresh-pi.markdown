---
author: Aaron Decker
comments: true
date: 2017-07-20
layout: post
slug: raspberry-pi-packet-capture
title: Raspberry Pi Packet Capturer
description: Setting up a new PI to capture packets.
---

![rapberry pi](/images/blog/pi-capturer.jpg){: .center-image }

## Before you can do anything, flash your PI it and enable SSH

  1. Download the minimal [Raspbian image](https://www.raspberrypi.org/downloads/raspbian/)
  2. Flash the card with the image using ["Etcher"](https://etcher.io/)
  3. Connect it to the network and boot it up.
  4. Scan the network to find it - "```nmap -sP 192.168.1.1-254```". That should list all of the IPs on your local network.
  5. OK, you found it but SSH doesn't work.
  6. Go grab an HDMI to DVI cable and hook your monitor up to it. Hook a keyboard up to it as well.
  7. Log in (pi/rasberry) and run "```sudo raspi-config```". The option to turn on SSH will be under interfaces.
  8. OK, restart the machine, and it should have the same IP it grabbed earlier.


## Capturing packets.

Okay now to capturing packets. Wait, that is why you have a pi right? OK, hook up [your wireless network adapter](http://amzn.to/2vwfWPt). Install aircrack ```sudo apt-get install aircrack-ng```. Now look at ```ifconfig```, it probably got wlan0. Set it into monitor mode:

```
pi@raspberrypi:~ $ sudo ifconfig wlan0 down && sudo iwconfig wlan0 mode monitor && sudo ifconfig wlan0 up
```

Okay great, now you can run "```airodump-ng wlan0```" with no other arguments to figure out what channel your own access point is listening on (right, we are just going to cap our own packets). So get the channel (for example, let's assume you are on channel 6) and then start airodump-ng back up on that specific channel while saving the packets.

```
sudo airodump-ng -c 6 -w mycapfilename wlan0
```

## Getting a WPA2 handshake

So probably you are using WPA2 and you need to capture a handshake in order to crack the password. Alright, great. The easiest way to do this will be to disconnect your phone and reconnect your phone to your wifi access point.

So probably you want to also know how you would deauthenticate the client and force the client to try to reconnect by itself. Well, that is actually pretty easy. In airodump you want to identify a client that is connected to your base station target. The activity will show up in the bottom section of the airodump. Just note the BSSID of the access point your trying to find a handshake for and note the mac addresses of the clients that connect to it.

![Example of my access point](/images/blog/my-access-point-annotated.png){: .center-image }

  1. BSSID of the target access point your want the handshake for (which you need to crack WPA2)
  2. ESSID of the client that is connected to your target access point (this is my phone)

[Now with these two things you can run aireplay-ng and deauthenticate the client.](https://www.aircrack-ng.org/doku.php?id=deauthentication)

The deauth will look something like this below. You can run it multiple times, or change the number of deauth attempts.

```
#  aireplay-ng -0 <times to send deauth> -a <target access point> -c <connected client> <your adapter ID>
# actual command below:

sudo aireplay-ng -0 5 -a C8:D7:19:94:AC:8E -c 68:C4:4D:98:D1:AB wlan0
```

Helpfully, airodump will notify you when it collects a handshake in the top right hand corner of the screen.

## Now crack the handshake

So now you have handshake! OK Great, go ahead and use SSH to copy the .cap file back onto your main workstation. Run "```aircrack-ng <your capture file here>```" and make sure that aircrack-ng can recognize the handshake for your access point. The next thing you will need to get is a dictionary file. There are lot of places you can get password lists, but keep in mind WPA requires an 8 char min password. [So I would find a dictionary of words that is geared toward WPA](http://www.wirelesshack.org/wpa-wpa2-word-list-dictionaries.html). It just needs to be a newline separated list of words in a text file.

When you are done finding your dictionary you can just pass it as an argument to aircrack-ng like so:

```
# example:
# aircrack-ng -w <path to wordlist> <path to capture file>

aircrack-ng -w ~/wordlists/wpa.txt ~/captures/mycapfilename.cap
```

You will get a cool looking screen and your CPU will be thrashed while aircrack tries passwords against the handshake.

![aircrack-ng screenshot](/images/blog/aircrack-ng.png){: .center-image }
