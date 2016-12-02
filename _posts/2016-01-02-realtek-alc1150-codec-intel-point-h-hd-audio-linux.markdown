---
author:Aaron Decker
comments: false
date: 2016-01-02 05:59:30+00:00
layout: post
link: http://ard.ninja/blog/realtek-alc1150-codec-intel-point-h-hd-audio-linux/
slug: realtek-alc1150-codec-intel-point-h-hd-audio-linux
title: Gigabyte GA-H170-GAMING 3 motherboard Audio and Linux
wordpress_id: 338
categories:
- Linux
---

**Note: The tl;dr of this is just use Ubuntu 15.10 and audio will work with the Gigabyte GA-H170-GAMING 3 motherboard out of the box!**


### A New Motherboard

I just got a new motherboard in order to do some long delayed upgrades to my desktop system and it ended up being a sort-of medium tier gaming oriented motherboard. I was pretty happy about the fact that it had a pretty nice onboard audio chipset because over the past year I have started to become a bit of an audiophile. I listen to a lot of classical music and Jazz and I have around a hundred of gigabytes of FLAC files in my collection. Anyway, point being: I really really wanted audio to work well under Linux but I didn't think about compatibility issues because I don't usually buy such new higher-end hardware.



### The First Problem That Really Was Not A Problem

On this particular motherboard the audio chipset is Intel and it is running the Realtek ALC1150 codec. Initially when I tried to run this using Linux mint 17 I also had a Radeon HD 6870 graphics card loaded on the system which happens to have HDMI audio that is also running an Intel chipset. The last time I used this graphics card with another motherboard I had the problem (in Windows and Linux actually) where the HDMI audio was being used as the default and I couldn't get it to switch back to the motherboard audio. So stupidly I made the assumption that this was again the problem!

I noticed that the HDMI audio was getting loaded correctly and showing up in my audio settings but the motherboard audio was not. At this time I did not really know how Linux audio subsystems worked- [I do now](http://tuxradar.com/content/how-it-works-linux-audio-explained). ALSA (Advanced Linux Sound Architecture) is the lowest level, then PulseAudio sits on top of that and finally your application will typically talk to pulse audio. As I understand it, ALSA loads the cards with some driver and makes them available to the system. If you look in /etc/modprobe.d/alsa-base.conf you can get an idea for how some of this works and you can even blacklist drivers or set additional options. When the card is loaded it will show up in ALSA and you can list loaded cards with the command "aplay -l". But my motherboard audio card was not showing up in ALSA! However it was definitely being recognized my the system when I ran "lsmod -v".

I tried various things - restarting ALSA, attempting to disable the HDMI audio card, going into the alsamixer utility and poking around among other things. Again at this point I thought that maybe it was some conflict between the cards that was preventing the motherboard card from being loaded. I realized thanks to lsmod that both devices are supposed to use the same driver module "snd-hda-intel". A lot of forums suggest that you should try to disable the driver from being loaded for the device you do not want to run, but I couldn't do this because both were using the same driver! I grew increasingly frustrated from this and finally decided to try to use Ubuntu 14.04 because in my experience Ubuntu is much better with hardware support I could perhaps figure out the correct configuration from there. Upon loading Ubuntu I saw that Ubuntu seemed to actually load the card into ALSA! So I could see the card in ALSA and I could select it in the mixer but still, no sound would ever come out. At this point I became convinced it was not a conflict but just a driver problem.




### A Driver Problem

So ubuntu 14.04 was reporting the card, ALSA was loading it, I could see it in the mixer but it was not playing any sound! "aplay -l" was listing this audio card as the following: "card 0: PCH [HDA Intel PCH], device 0: ALC1150 Analog [ALC1150 Analog]". I googled the ALC1150 Codec and found that it was a Realtek codec and that Realtek had some drivers written for linux. I tried these and also found that they did not help, but I was very confused on how the codec related to the chipset and how this came into play with the drivers and ALSA. It was all very mysterious and still is actually. Anyway, I tried everything I could think as well as everything various Linux forums could think of with the drivers.

I went to work the next day and though about it, read some forums, talked to some co-workers even. I read some discouraging things on the forums where people simply recommended buying a dedicated audio board [from the known working list](http://www.alsa-project.org/main/index.php/Matrix:Main). That seems like giving up to me. Somebody I work with said something about how he thought that the new drivers come out pretty quickly for linux and didn't see why I was having so many issues. Well I was using 14.04 (15.10 is the newest) so this gave me the idea to try 15.10, even though I always try to use the LTS version but honestly this is just a habit I got from doing dev-ops work and doesn't make a lot of sense for the desktop.



### My Solution

To bring this story to a close the audio worked out of the box with 15.10 - I actually figured that the LTS versions had updates to their drivers so I never considered this could be a problem. The other thing is that it could have been a kernel bug that was fixed in the new 15.10 version. Not a very intellectually satisfying conclusion, I have to admit. Either way this is the scariest thing about desktop Linux to me: even a very small problem often has a very complex cause and or solution and often times the quickest and most sure way to fix something is either switch distro or upgrade the OS version. However I am committed to running Linux as my primary OS due to my web development work so the only solution is to just get more overall knowledge about the Linux OS in general which is actually difficult because so much just does actually work out of the box but when you do have a problem it can be nearly impossible to solve quickly.

And as a final note, yes I am still running Ubuntu 15.10. I got rid of the Unity desktop and loaded up Gnome 3 which I actually like a lot, so I will be using this instead of Mint. I feel a bit safer with Ubuntu in general given the larger user base and better support in the forums.
