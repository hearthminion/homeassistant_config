# Lights Package

## Description

This package manages the lights.

The lights are configured into several modes:
- Circadian
- Darken
- Migraine
- Guests (Not yet implemented)
- Migraine (Sleeping) (Not yet implemented)
- Night Out (Not yet implemented)
- Other (Not yet implemented)

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
#### [Automation](https://www.home-assistant.io/docs/automation/)
- Toggle Adaptive Lighting Brightness switch if autobrightness binary sensor changes state
- Turn off Adaptive Lighting Brightness switch if Hue Dimmer Switch buttons 2 or 3 are pressed.
- Toggle Adaptive lighting based on if Circadian Mode is true or false
- Run [Update HomeAssistant Scene](#Update Home Assistant Scene) script every 5 minutes

#### [Input Select]
#### [Rest Command](https://www.home-assistant.io/integrations/rest_command/)
#### [Scenes](https://www.home-assistant.io/integrations/scene/)
##### HomeAssistant

This scene is managed by HomeAssistant it's settings are updating throughout the day depending on the light mode that is set.

##### Darken

This sets the lights to Red at 25% brightness.  Inspired by Navy's "Darken Ship" interior lighting for nighttime.

xy_color:
  - 0.6915
  - 0.3083
  
##### Migraine

This sets the lights to Green at 25% brightness.

xy_color:
  - 0.17
  - 0.7

#### [Scripts](https://www.home-assistant.io/docs/scripts/)

##### Update Home Assistant Scene

This updates the 'HomeAssistant' scene on the Hue Bridge.

- If the lighting mode is 'Circadian' it runs every 5 minutes, and updates the color_temp and brightness to stay in sync with adaptive lighting.
- If the lighting mode is 'Migraine' ... (TBD)
  I personally like the lights to be Green at 25% brightness.  However, if I am in a room by myself, I do not want to plunge everyone else in the house into dim green lighting.
  
- If the lighting mode is 'Darken' it runs once and sets the lights to Red at 25% brightness.

- If the lighting mode is 'Guest' I do not want adaptive lighting to decrease brightness after sunset.  Remaining requirements are TBD.  Thinking about a slow decrease in brightness say 20% over a 3 hr period starting at sunset.



##### Update Darken Scene
This is not run very often, but it is there to ensure that on the Hue Bridge xy_color is set as per [Darken](#Darken)

##### Update Migraine Scene
This is not run very often, but it is there to ensure that on the Hue Bridge xy_color is set as per [Migraine](#Migraine)

#### [Templates](https://www.home-assistant.io/integrations/template/)

##### Binary Sensors
- autobrightness: Returns true if the lights brightness is +/- 4% of the adaptive lighting brightness setting, else returns false.
- color_mode: Returns true if the lights in 'xy_color' mode, else return false.
- circadian_mode: Returns True if input_select.lighting_mode == 'Circadian' else returns false.

##### Sensors
- color: Returns lights xy_color value.


### Philips Hue Configuration

#### Groups

Each light fixture is created as a zone.
Each room is created as a room.
Each Bridge has a zone for all lights.

Rooms and Zones are name in the following manner:

2 letters floor: MF or BF
1 number: Hub # for that floor

Room(#)

Fixture#

Example:
MF1: Bedroom1 CF1 = Main Floor, Hub1, Bedroom1, Ceiling Fixture 1
BF1: Den Lamp1 = Basement Floor, Hub1, Den, Lamp 1

In the home assistant configuration, I rename the entity ids to match:
light.mf1_bedroom1_cf1
light.bf1_den_lamp1

#### Scenes
Each group of lights has 10 scenes defined, the 7 basic hue scenes, plus 3 I created.
##### Default Hue Scenes
- [Bright](#Bright)
- [Concentrate](#Concentrate)
- [Dimmed](#Dimmed)
- [Energize](#Energize)
- [Nightlight](#Nightlight)
- [Read](#Read)
- [Relax](#Relax)

##### Custom Scenes
- [HomeAssistant](#HomeAssistant)
- [Darken](#Darken)
- [Migraine](#Migraine)

## Features
### Features
#### Automations
#### Scenes
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

## Default Hue Dynamic Scenes

These are scenes with effects

### Candle
### Fireplace

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
- [Philips hue dynamic scenes](https://community.home-assistant.io/t/philips-hue-dynamic-scenes/345000)
- [Hue scenes mimicked in Ha (and on Buttons, was Tiles)](https://community.home-assistant.io/t/hue-scenes-mimicked-in-ha-and-on-buttons-was-tiles/93570/27)
