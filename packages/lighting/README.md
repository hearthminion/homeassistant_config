# Lights Package

## Description

## Installation
### Home Assistant Custom Integrations
#### [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting)
Author: basnijholt

The adaptive_lighting platform changes the settings of your lights throughout the day. It uses the position of the sun to calculate the color temperature and brightness that is most fitting for that time of the day. Scientific research has shown that this helps to maintain your natural circadian rhythm (your biological clock) and might lead to improved sleep, mood, and general well-being.

### Other tools used
#### [Color Thief](https://lokeshdhakar.com/projects/color-thief/)
#### [APK Tool](https://ibotpeaches.github.io/Apktool/)
#### uuidgen

Used to generate uuids for automations, scenes, etc.

### Home Assistant Components
#### [Automation]
##### Disable Brightness control during the day
##### Enable Brightness control during the evening
##### Disable Circadian Lighting
##### Enable Circadian Lighting

#### [Input Select]
#### [Rest Command](https://www.home-assistant.io/integrations/rest_command/)
#### [Scenes]
#### [Templates]


## Features
### Features
#### Automations
#### Scenes
##### Darken Room
#### Switches

## Default Hue Scene Definitions

### Bright
- color_temp: 367
- brightness: 255

### Concentrate
- color_temp: 230
- brightness: 255

### Dimmed
- color_temp: 369
- brightness: 76

### Energize
- color_temp: 156
- brightness: 255

### Nightlight
- color_temp: 454
- brightness: 1

### Read
- color_temp: 343
- brightness: 255

### Relax
- color_temp: 447
- brightness: 145

## Default Hue Scene Photos

Images come from [Unsplash](https://unsplash.com/)

- Amber Bloom
  by:
- Arctic Aurora
  by: David Gil
- Autumn Gold
  by: Dana Moos
- Blood Moon
  by: Andrea Reiman
- Blue Lagoon
  by:
- Blue Planet
  by:
- Chinatown
  by: Pascal Terjan
- City of Love
  by:
- Color Burst
  by:
- Crystaline
  by:
- Disturbia
  by:
- [Emerald Isle](https://unsplash.com/photos/cuhu-aAdzs0)
  by: [Jasmin Causevic](https://unsplash.com/@duplich)
- Fairfax
  by:
- Festive Fun
  by:
- Forest Adventure
  by:
- Frosty Dawn
  by:
- [Galaxy](https://unsplash.com/photos/QeoXkIesiCo)
  by: [Manouchehr Hejazi](https://unsplash.com/@patrol)
- Glitz and glam
  by:
- [Golden Pond](https://unsplash.com/photos/b4SRwTQget8)
  by: [Claudia Viloria](https://unsplash.com/@viloria)
- Golden Star
  by:
- Hal
  by:
- [Honolulu](https://unsplash.com/photos/2-Bq_AGZyr8)
  by: [Amit Nayak](https://unsplash.com/@amitnayak)
- Ibiza
  by: Michal Grosicki
- Lake Placid
  by:
- Lake Mist
  by: [Ales Krivec](https://unsplash.com/@aleskrivec)
- Lily
  by:
- Lovebirds
  by:
- Magento
  by:
- Midsummer Sun
  by: [Susanne Nilsson](https://unsplash.com/@kosthjalpen/likes)
- Midwinter
  by:
- [Moonlight](https://unsplash.com/photos/6msS8vT5pzw)
  by: [Benjamin Child](https://unsplash.com/@bchild311)
- Mountain Breeze
  by:
- Motown
  by:
- [Nebula](https://unsplash.com/photos/33FlT2A83H4)
  by: [Ernest Karchmit](https://unsplash.com/@ekarchmit)
- [Ocean Dawn](https://unsplash.com/photos/EEDLURXCpqg)
  by: [Anastasia Taioglou](https://unsplash.com/@thenata)
- Orange Fields
  by:
- [Osaka](https://unsplash.com/photos/saxby7Bioxc)
  by: [Alex Knight](https://unsplash.com/@agk42)
- Palm Beach
  by:
- Painted Sky
  by:
- Promise
  by:
- [Ruby Glow](https://unsplash.com/photos/nE2gf1scItI)
  by: [Martin Jernberg](https://unsplash.com/@martinjernberg)
- Ruby Romance
  by:
- Rosy Sparks
  by:
- Savanna Sunset
  by: Lady DragonflyCC
- Smitten
  by:
- [Soho](https://unsplash.com/photos/RnCPiXixooY)
  by: [Efe Kurnaz](https://unsplash.com/@efekurnaz)
- Silent Night
  by:
- Spring Blossom
  by: Oimax
- Spring Lake
  by: Shirsendu Nayak
- [Starlight](https://unsplash.com/photos/ln5drpv_ImI)
  by: [Vincentiu Solomon](https://unsplash.com/@vincentiu)
- [Sunday Morning](https://unsplash.com/photos/S3UCfaKTNZQ)
  by: [Carsten Stalljohann](https://unsplash.com/@pascelcrow)
- [Sundown](https://unsplash.com/photos/1HplMDoRvTo)
  by: [Cristina Gottardi](https://unsplash.com/@cristina_gottardi)
- Tokyo
  by:
- Tropical Twilight
  by: Roman Till
- Tyrell
  by:
- Under the Tree
  by:
- Vapor Wave
  by:
- Winter Beauty
  by:
- Winter Mountain
  by:

# References
- [DIY Hue Scenes in Home Assistant using the deCONZ integration](https://www.jeroendruwe.be/diy-hue-scenes-in-home-assistant-using-the-deconz-integration/) Jeroen Drewé
- [Scenes and Groups](https://community.home-assistant.io/t/scenes-and-groups/41948)
- [Entities Card - Setting Hue Scene](https://community.home-assistant.io/t/entities-card-setting-hue-scene/137886)
- [Using Home Assistant and Philips Hue to create a full colour sunrise](https://149walnut.com/2017-12-using-home-assistant-and-philips-hue-to-create-a-full-colour-sunrise-alarm-clock/)
- [Turning on a scene directly from a Lovelace button](https://community.home-assistant.io/t/turning-on-a-scene-directly-from-a-lovelace-button/263056)
- [Scenes operating as a switch](https://community.home-assistant.io/t/scenes-operating-as-a-switch/237228)
- [Scenes - Home Assistant](https://www.home-assistant.io/integrations/scene/)
- [Philips hue dynamic scenes](https://community.home-assistant.io/t/philips-hue-dynamic-scenes/345000)
- [Hue scenes mimicked in Ha (and on Buttons, was Tiles)](https://community.home-assistant.io/t/hue-scenes-mimicked-in-ha-and-on-buttons-was-tiles/93570/27)
