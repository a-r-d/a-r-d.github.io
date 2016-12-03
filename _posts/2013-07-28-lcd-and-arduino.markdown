---
author: Aaron Decker
comments: true
date: 2013-07-28 05:26:52+00:00
layout: post
link: http://ard.ninja/blog/lcd-and-arduino/
slug: lcd-and-arduino
title: LCD and Arduino
description: My experiments with buying a little 20x4 LCD screen to use with an arduino
wordpress_id: 222
---

So I just grabbed a large 20x4 LCD screen off of Amazon that is supposed to compatible with arduino ([LCD Module for Arduino 20 x 4, White on Blue](http://www.amazon.com/gp/product/B003B22UR0/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B003B22UR0&linkCode=as2&tag=ultralightgea-20)![](http://ir-na.amazon-adsystem.com/e/ir?t=ultralightgea-20&l=as2&o=1&a=B003B22UR0)). With very few snags I was up an running in no time actually...

Things to note: This only requires the use the 5v power provided by the Arduino Uno and 2 analog pins. [This guy on the arduino forums](http://forum.arduino.cc/index.php?topic=128635.0) wrote up an amazing walk-through that I highly suggest you read.

Things you may want to know from me:

1. Yes, I did have to bend the pins.
2. It is really bright!
3. [The scanner program](http://playground.arduino.cc/Main/I2cScanner) detected the IC2 device at 0x27 for me.
4. When I copied the library over into my library directories it did not import it automatically. So when I went to run [the test program](https://bitbucket.org/celem/sainsmart-i2c-lcd/src/3adf8e0d2443/sainlcdtest.ino) it would not compile! I had to go to "Sketch" -> "Import Library" and pick it out...
5. here is another example test program that worked with the exact model from Amazon listed above (ordered 7/23/13)...

{% highlight cpp %}

#include
#include
#include
#include
#include
#include
#include
#include

/*
** Example Arduino sketch for SainSmart I2C LCD2004 adapter for HD44780 LCD screens
** Readily found on eBay or http://www.sainsmart.com/
** The LCD2004 module appears to be identical to one marketed by YwRobot
**
** Address pins 0,1 & 2 are all permenantly tied high so the address is fixed at 0x27
**
** Written for and tested with Arduino 1.0
** This example uses F Malpartida's NewLiquidCrystal library. Obtain from:
** https://bitbucket.org/fmalpartida/new-liquidcrystal
**
** Edward Comer
** LICENSE: GNU General Public License, version 3 (GPL-3.0)
**
** NOTE: TEsted on Arduino NANO whose I2C pins are A4==SDA, A5==SCL
*/
#include
#include
#include

#define I2C_ADDR    0x27  // Define I2C Address where the PCF8574A is
#define BACKLIGHT_PIN     3
#define En_pin  2
#define Rw_pin  1
#define Rs_pin  0
#define D4_pin  4
#define D5_pin  5
#define D6_pin  6
#define D7_pin  7

int n = 1;

LiquidCrystal_I2C       lcd(I2C_ADDR,En_pin,Rw_pin,Rs_pin,D4_pin,D5_pin,D6_pin,D7_pin);

void setup()
{
  lcd.begin (20,4);

// Switch on the backlight
  lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
  lcd.setBacklight(HIGH);
  lcd.home ();                   // go home

  lcd.print("Yay First Line!");  
  lcd.setCursor ( 0, 1 );        // go to the 2nd line
  lcd.print("What happens if we write past the end of the line?");
  lcd.setCursor ( 0, 2 );        // go to the third line
  lcd.print("LCDs are cool");
  lcd.setCursor ( 0, 3 );        // go to the fourth line
  lcd.print("Iteration No: ");
}

void loop()
{
  lcd.setCursor (14,3);        // go col 14 of line 3
  lcd.print(n++,DEC);
  lcd.setBacklight(HIGH);     // Backlight on
  delay(3000);
}

{% endhighlight %}
