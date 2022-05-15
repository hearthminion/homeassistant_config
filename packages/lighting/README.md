# Lights Package

## Description

This package manages the lights.

### Light Modes

#### Circadian

This is the default mode.  It is part of the daily routine.

#### Darken

Partially implemented, the scene exists.  It too is part of the daily routine.  While adaptive lighting provides a "sleep" mode, to get the color I want, I would need to configure adaptive lighting to use "xy" mode for adjusting the light's color temperature.  In so doing, I lose the ability to check for other color scenes for disabling the color adjustment based on an "xy" mode alone.  The check becomes significantly more complicated.

#### Migraine

This is the most complicated mode.  It's a mixture of Circadian, and green lights.

Once triggered, an automation starts that does the following actions:
1. While current circadian color temperature is above 3500K, color adjustments are disabled.
2. If light is on, and any light in the room is green, it is turned green.
3. If light is on, and light is in "ct" mode, and color temperature is above 3500K: light color temperature set to 3500K.

The goal is to not put everyone in the house into green lighting, while providing green lighting where desired.


#### Guests (Not yet implemented)
#### Migraine (Sleeping) (Not yet implemented)
#### Night Out (Not yet implemented)
- Other (Not yet implemented)



## Installation
### Home Assistant Custom Integrations
#### [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting)
Author: basnijholt

The adaptive_lighting platform changes the settings of your lights throughout the day. It uses the position of the sun to calculate the color temperature and brightness that is most fitting for that time of the day.

I selected this over [Circadian Lighting](https://github.com/claytonjn/hass-circadian_lighting) because this integration has a switch to toggle brightness adjustments, and Circadian Lighting does not.  This resulting in an automation that rather than switching brightness control on and off, would require two circadian switches per light fixture, one with brightness adjustment on and on off, and the automation would swap which circadian switch was turned on at any given time.

### Other tools used
#### [Color Thief](https://lokeshdhakar.com/projects/color-thief/)
#### [APK Tool](https://ibotpeaches.github.io/Apktool/)
#### uuidgen

Used to generate uuids for automations, scenes, etc.

### Home Assistant Components
#### [Automation](https://www.home-assistant.io/docs/automation/)
- Toggle Adaptive Lighting Brightness switch if autobrightness binary sensor changes state
- Turn off Adaptive Lighting Brightness switch if Hue Dimmer Switch buttons 2 or 3 are pressed.
- Toggle Adaptive lighting switch if autocolortemp binary sensor changes state
- Toggle Adaptive Lighting based on bulb state: 'xy_color' mode (Off) or 'colortemp' mode (On)
- Toggle Adaptive lighting based on if Circadian Mode is true or false
- Turn on Migraine Mode if lights are set manually set to green
- Turn on [Light Previously Green](#light-previously-green) if Migraine Mode is activated
- Turn on [Light Previously Green](#light-previously-green) at Midnight
- Set Light mode to Circadian at 4 am
- Run [Update HomeAssistant Scene](#update-home-assistant-scene) script every 5 minutes

#### [Input Boolean](https://www.home-assistant.io/integrations/input_boolean/)
##### Light Previously Green

This tracks if a light has been turned green at some point during the day.

#### [Input Select](https://www.home-assistant.io/integrations/input_select/)
##### Light Mode

Tracks current lighting mode

#### [Rest Command](https://www.home-assistant.io/integrations/rest_command/)
##### Update HomeAssistant Scene
This updates all lights in the group when all lights have the exact same configuration.

##### Update HomeAssistant Scene Complex
This updates lights when each light has a different configuration.

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
  - 0.23
  - 0.698
  
Note: Hue Color Gamut "Green" has xy_color of [0.17,0.7].  Which corresponds to approximately 510nm wavelength (RGB: 0,255,0).  The wavelength [tested](https://academic.oup.com/brain/article/139/7/1971/2464334) was 530nm with an error of +/- 10nm.  530nm is closer to RGB: 94, 255,0, which corresponds to xy_color of [0.23,0.698].  Using [0.23,0.698] puts the bulbs theoretically in the middle of the range.  Taking into consideration that I don't expect the bulbs to be perfectly calibrated, this increases the odds that the color produced will fall close if not within the +/- 10nm range.

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
- 2 letters floor: MF or BF
- 1 number: Hub # for that floor
- Room(#)
- Fixture#

Examples:
- MF1: Bedroom1 CF1 = Main Floor, Hub1, Bedroom1, Ceiling Fixture 1
- MF2: Den CF1 = Main Floor, Hub2, Den, Ceiling Fixture 1
- BF1: Den Lamp1 = Basement Floor, Hub1, Den, Lamp 1

In the home assistant configuration, I rename the entity ids to match:
light.mf1_bedroom1_cf1
light.mf2_den_cf1
light.bf1_den_lamp1

#### Scenes
Each group of lights has 8-12 scenes defined, the 7 basic hue scenes, plus 3 I created.
##### Default Hue Scenes
- [Bright](#Bright)
- [Concentrate](#Concentrate)
- [Dimmed](#Dimmed)
- [Energize](#Energize)
- [Nightlight](#Nightlight)
- [Read](#Read)
- [Relax](#Relax)
- [Candle](#Candle) If applicable (Newer bulbs only)
- [Fireplace](#Fireplace) If applicable (Newer bulbs only)

##### Custom Scenes
- [HomeAssistant](#HomeAssistant)
- [Darken](#Darken) If applicable (Color bulbs only)
- [Migraine](#Migraine) If applicable (Color bulbs only)

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
- color_temp: 500 (Color Bulbs) or  454 (Ambiance Bulbs)
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

Images come from [Unsplash](https://unsplash.com/) or [Flickr](https://flickr.com)

- Amber Bloom
  by: Aaron Burden
- [Arctic Aurora](https://flic.kr/p/377PBM)
  by: [David Gil](https://www.flickr.com/photos/deivis/)
- [Autumn Gold](https://flic.kr/p/8r8Pmd)
  by: [Dana Moos](https://www.flickr.com/photos/dana_moos)
- Blood Moon
  by: Andrea Reiman
- Blue Lagoon
  by: Sarah Cassady
- Blue Planet
  by: Shaah Shahidh
- Chinatown
  by: Pascal Terjan
- City of Love
  by: Fab Lentz
- Color Burst
  by: Gregoire Bertaud
- Crystal line
  by: Aaron Burden
- Disturbia
  by: Milada Vigerova
- [Emerald Isle](https://unsplash.com/photos/cuhu-aAdzs0)
  by: [Jasmin Causevic](https://unsplash.com/@duplich)
- Fairfax
  by: Conner Murphy
- Festive Fun
  by: Benjamin Muntz
- Forest Adventure
  by: Nathan Queloz
- Frosty Dawn
  by: Laura Taylor
- [Galaxy](https://unsplash.com/photos/QeoXkIesiCo)
  by: [Manouchehr Hejazi](https://unsplash.com/@patrol)
- Glitz and glam
  by: Sharon McCutcheon
- [Golden Pond](https://unsplash.com/photos/b4SRwTQget8)
  by: [Claudia Viloria](https://unsplash.com/@viloria)
- Golden Star
  by: Aaron Burden
- Hal
  by: Cedric Klei
- [Honolulu](https://unsplash.com/photos/2-Bq_AGZyr8)
  by: [Amit Nayak](https://unsplash.com/@amitnayak)
- Ibiza
  by: Michal Grosicki
- Lake Placid
  by: Mikkel Schmidt
- Lake Mist
  by: [Ales Krivec](https://unsplash.com/@aleskrivec)
- Lily
  by: Kat Jayne
- Lovebirds
  by: Paul Cusick
- Magento
  by:
- [Midsummer Sun](https://flic.kr/p/AqoAwo)
  by: [Susanne Nilsson](https://www.flickr.com/photos/infomastern/)
- Midwinter
  by: Peter Lewis
- [Moonlight](https://unsplash.com/photos/6msS8vT5pzw)
  by: [Benjamin Child](https://unsplash.com/@bchild311)
- Mountain Breeze
  by: Oswaldo Martinez
- Motown
  by: Greyson Joralemon
- [Nebula](https://unsplash.com/photos/33FlT2A83H4)
  by: [Ernest Karchmit](https://unsplash.com/@ekarchmit)
- [Ocean Dawn](https://unsplash.com/photos/EEDLURXCpqg)
  by: [Anastasia Taioglou](https://unsplash.com/@thenata)
- Orange Fields
  by: Toomas Tartes
- [Osaka](https://unsplash.com/photos/saxby7Bioxc)
  by: [Alex Knight](https://unsplash.com/@agk42)
- Palm Beach
  by: Steven Pahel
- Painted Sky
  by: Tandem X Visuals
- Promise
  by: Sereja Ris
- [Ruby Glow](https://unsplash.com/photos/nE2gf1scItI)
  by: [Martin Jernberg](https://unsplash.com/@martinjernberg)
- Ruby Romance
  by: Jamie Street
- Rosy Sparks
  by: Wout Vanacker
- [Savanna Sunset](https://flic.kr/p/aA9YwS)
  by: [Lady DragonflyCC](https://www.flickr.com/photos/ladydragonflyherworld/)
- Smitten
  by: Freestocks
- [Soho](https://unsplash.com/photos/RnCPiXixooY)
  by: [Efe Kurnaz](https://unsplash.com/@efekurnaz)
- Silent Night
  by: Christina Winter
- [Spring Blossom](https://flic.kr/p/bxTCdj)
  by: [Oimax](https://www.flickr.com/photos/oimax/)
- [Spring Lake](https://flic.kr/p/yG45xm)
  by: [Shirsendu Nayak](https://www.flickr.com/photos/9s9)
- [Starlight](https://unsplash.com/photos/ln5drpv_ImI)
  by: [Vincentiu Solomon](https://unsplash.com/@vincentiu)
- [Sunday Morning](https://unsplash.com/photos/S3UCfaKTNZQ)
  by: [Carsten Stalljohann](https://unsplash.com/@pascelcrow)
- [Sundown](https://unsplash.com/photos/1HplMDoRvTo)
  by: [Cristina Gottardi](https://unsplash.com/@cristina_gottardi)
- Tokyo
  by: Benjamin Hung
- [Tropical Twilight](https://flic.kr/p/qU66ru)
  by: [Roman Till](https://www.flickr.com/photos/130079987@N02/)
- Tyrell
  by: Drew Graham
- Under the Tree
  by: Hert Niks
- Vapor Wave
  by: Stephen Johnson
- Winter Beauty
  by: Mikael Kristenson
- [Winter Mountain](https://flic.kr/p/xscjjY)
  by: [Image Catalog](https://www.flickr.com/photos/image-catalog/)

# References
- [DIY Hue Scenes in Home Assistant using the deCONZ integration](https://www.jeroendruwe.be/diy-hue-scenes-in-home-assistant-using-the-deconz-integration/) Jeroen Drewé
- [Scenes and Groups](https://community.home-assistant.io/t/scenes-and-groups/41948)
- [Entities Card - Setting Hue Scene](https://community.home-assistant.io/t/entities-card-setting-hue-scene/137886)
- [Using Home Assistant and Philips Hue to create a full colour sunrise](https://149walnut.com/2017-12-using-home-assistant-and-philips-hue-to-create-a-full-colour-sunrise-alarm-clock/)
- [Turning on a scene directly from a Lovelace button](https://community.home-assistant.io/t/turning-on-a-scene-directly-from-a-lovelace-button/263056)
- [Scenes operating as a switch](https://community.home-assistant.io/t/scenes-operating-as-a-switch/237228)
- [Philips hue dynamic scenes](https://community.home-assistant.io/t/philips-hue-dynamic-scenes/345000)
- [Hue scenes mimicked in Ha (and on Buttons, was Tiles)](https://community.home-assistant.io/t/hue-scenes-mimicked-in-ha-and-on-buttons-was-tiles/93570/27)
