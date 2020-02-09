# Better presence 
I wanted to make a better precense in code rather than in Hass configurations. Felt must be way easier to get the advanced things I want.

Checkout 
https://philhawthorne.com/making-home-assistants-presence-detection-not-so-binary/ as inspiration

Basically I want the state to go:

```
Home->Just left->Away->Zone

Home->Just left->Home

Away->Just arrived->Home

```

Now I can trigger a welcome message on just arrived but it will not trigger if I was temporarily Just left and got Home again.
You can easily customize the state names in globals.py
## Group functionality
You will have to have your devices in a group. Recommed one gps, like owtracks or gpstracker, one bluetooth and one wifi like nmap. 3 devices like this gives the best result imo. 

The logic is: If bluetooth or wifi device is 'home' the whole group is considered home. if bluetooth and wifi are 'not_home' and gps are home and been recently updated then the group is home, else group is considered 'not_home' 

## Enity picture
If any of the devices has a enity_picture then the tracker gets that picture too
## Tracking of gps coordinates
The sensor will have the same tracking coordinates as the gps device in group. Make sure you only have one gps device!!!
## Cofigure in apps.yaml
```
app_presence_tomas:
  module: presence
  class: a_better_presence
  name: presence_tomas                # name of the device in Hass
  timer: 600                          # timeout in seconds from just arrived to home and just left to away
  update_time: 7200                   # how old reported values get to be before reporting not_home (2hr)
  group_devices: group.tomas_devices  # The group that contains the trackked devices

```

## Configuring triggers on states

*You will have to use the condition like below not to make the trigger fire 
when you reboot the device or hass*

Example below sends a message through script when state changes except when from_state is nothing wich is the case when it starts.

```
automation:
  - alias: Send message on away-home notice Tomas
    trigger:
      - platform: state
        entity_id: sensor.presence_tomas 
    condition:
      - condition: template
        value_template: "{{ trigger.from_state != None }}"
    action:
      service: script.notify
      data_template:
        tell: th
        title: "Tomas status {{trigger.to_state.state}}"
        message: "Tomas has changed status for tracker {{trigger.to_state.state}}"    
```