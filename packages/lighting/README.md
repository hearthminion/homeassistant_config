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

All images come from [Unsplash](https://unsplash.com/)

### Galaxy
- image: https://unsplash.com/photos/QeoXkIesiCo
  by: Manouchehr Hejazi
  https://unsplash.com/@patrol

### Golden Pond
- image: https://unsplash.com/photos/b4SRwTQget8
  by: Claudia Viloria
  https://unsplash.com/@viloria

# References
- [DIY Hue Scenes in Home Assistant using the deCONZ integration](https://www.jeroendruwe.be/diy-hue-scenes-in-home-assistant-using-the-deconz-integration/) Jeroen Drewé
