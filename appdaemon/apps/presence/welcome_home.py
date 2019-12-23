from base import Base
from globals import GlobalEvents, presence_state, PEOPLE
from typing import Tuple, Union
import datetime, time
import secrets
"""
Class ProximityManager handles automation depending how far a person are to a zone

Following use-cases are implemented:
- If One or more proximity sensors within a range and specific time of day
  send event

"""
class WelcomeHomeManager(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize() # Always call base class
        self._door_sensor = self.args.get('door_sensor', str)
        self._tts_device = self.args.get('tts_device', str)
        self._was_away = {} # The person needs to be away before can get another announcement

        self.log(self.datetime())
        for person in PEOPLE:
            self.listen_state(
                self.__on_presence_changed, entity=PEOPLE[person]['device_tracker'], attribute='all', person=person)
            self._was_away[person] = True

        self.listen_state(
            self.__on_door_sensor_changed, new='on', old='off', entity=self._door_sensor)

    def __on_door_sensor_changed(
        self, entity: Union[str, dict], attribute: str, old: dict,
        new: dict, kwargs: dict) -> None:

        for person in PEOPLE:
            state = self.get_state(PEOPLE[person]['device_tracker'])
            if state == presence_state['just_arrived']:
                self.__announce_welcome_home(person)

    def __on_presence_changed(
        self, entity: Union[str, dict], attribute: str, old: dict,
        new: dict, kwargs: dict) -> None:
        if old is not None and new['state'] == old['state']:
            return # We dont care about updates in attributes

        person = kwargs['person']
        # If the person hast just arrived and the door sensor i just been triggered then
        if new['state'] == presence_state['just_arrived']:
            door_sensor_state = self.get_state(self._door_sensor, attribute='all')
            
            last_changed = self.convert_utc(door_sensor_state.get('last_changed', str))
            time_lapsed = datetime.datetime.now(datetime.timezone.utc) - last_changed
      
            if time_lapsed.days == 0 and time_lapsed.seconds < 60*5: # 5 minutes
                self.__announce_welcome_home(person)

        elif new['state']!=presence_state['just_left'] and new['state']!=presence_state['home']:
            self._was_away[person] = True # We set this to True to be able to announce again

    def __announce_welcome_home(self, person:str)->None:
        if self._was_away[person] is True: # Only persons that been away we announce
            self._was_away[person] = False
            self.__trigger_message(person)
 
    def __trigger_message(self, person:str)->None:
        
        message = secrets.choice(
            [
                "Va fan är du hemma {}, måste skynda mig att ta bort knarket.".format(person),  
                "{} är hemma, zingo sluta att skälla! Sluta att skälla zingo! jag blir tokig! Sluta skälla för i helvete!".format(person),
                "När man inte trodde det kunde bli sämre, så kom {} hem.".format(person),
                "{}, gör disken för i helvete.".format(person),
                "{}, sluta lata dig, be mig dra en skämt i stället!".format(person),
                "Men oj vad det ska vara fint värre när {} kommer hem. Fattar inte grejen.".format(person),
                "Fan var det luktar illa! {} stäng munnen!".format(person),
                "{} du tro visst att du är nått. Har nyheter till dig. Du betyder inte ett skit för mig!".format(person),
                "Jag älskar dig {}, ha ha ha skojar bara!".format(person),
                "Ett mirakel har skett! {} hittade hem!".format(person),
                "Välkomen hem {} hoppas du haft en fin dag så här långt!".format(person),
                'Hoppas du haft det bra {}, välkommen hem ska du vara!'.format(person),                
                'Vad roligt att du kommer hem nu {}, här är allt lugnt.'.format(person),       
                '{} är hemma, så roligt! Jag har haft så tråkigt hela dagen instängd i den här högtalaren'.format(person),       
                '{}, {}, {}, tre ord av lycka. Välkommen!'.format(person, person, person),       
                'Jag har något att erkänna för dig {}, jag har längtat hela dagen efter dig.'.format(person),       
                'Alla som älskar {}, klappar nu! Klapp klapp. Härligt att se dig hemma igen!'.format(person),       
                'Superkul att jag får hälsa familjen välkommen, speciellt dig {}.'.format(person),       
                'Om jag kunde sjunga skulle jag sjunga en trudilutt för nu är {} här!'.format(person),       
                'Även om jag är en artificiell intelligens så har jag faktiskt känslor {}, lämna mig inte ensam så här.'.format(person),       
                'Prata inte med mig {}, jag är sur.'.format(person),       
                'Tjena tjena mittbena {}, dags att komma hem nu?'.format(person),       
                'Hej {}, det enda som slår högre att du kommer hem är att du åker.'.format(person),       
                'Tror det började precis lukta illa här. Vänta nu förstår jag. {} kom hem.'.format(person),       
                'Vad bra att du kommer hem {}. Behöver råd i kärleksbekymmer. Jag är kär i en TV.'.format(person),       
                'Nämen va fan, det är ju du {}, jag har faktistk haft tråkigt instängd i denna högtalare.'.format(person),       
                'Jag blir så glad {} att jag vill sjunga, men det kan jag inte. Jag är ju för helvete en maskin.'.format(person),       
                'Zingo blir glad, jag blir glad och till och med fågeln som borde ha dött för länge sen blir glad att se dig {}.'.format(person),       
                'Vet ni vilken som är min favorit person? Det är förstås {}, och nu är du hemma. Hurra!'.format(person),       
                '{}, hoppas din dag varit bra hittils. Välkommen!'.format(person) 
            ])
        # if person == 'Melker':
        #     message.extend([
        #         "Tjena {},  hoppas du haft en fin dag så här långt!".format(person), 
        #     ])

        self.tts_manager.set_volume_level('0.9', media_player=self._tts_device)
        self.tts_manager.speak(message, media_player=self._tts_device)