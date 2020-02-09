from base import Base
from globals import PEOPLE, presence_state
from typing import Tuple, Union
"""
Class LowBatteryManager manages the low battery warning TTS 


"""
class LowBatteryManager(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize() # Always call base class

        self._people = self.args.get("people", {})
        self._low_bat_level = int(self.args.get("battery_level_low", "15"))
        self._tts_device = self.args.get("tts_device", "media_player.house")

        for person in self._people:
            self.log("Setup tracker {}".format(PEOPLE[person]['device_tracker']))
            self.listen_state(
                self.__on_tracker_changed, 
                entity=PEOPLE[person]['device_tracker'],
                attribute="all",
                person=person
            )

    def __on_tracker_changed(
            self, entity: Union[str, dict], attribute: str, old: dict,
            new: dict, kwargs: dict) -> None:

        if old is None:
            return

        person = kwargs['person']
        batt_level = int(new["attributes"].get("battery_level", "100"))
        old_bat_lev = int(old["attributes"].get("battery_level", "100"))
        state = new["state"]
        
        if batt_level != old_bat_lev and self.now_is_between("07:00:00", "22:30:00"):
            self.log("{} changed battery status from {} to {}".format(entity, old_bat_lev, batt_level))

        if old_bat_lev > self._low_bat_level and \
            batt_level<=self._low_bat_level and \
            state==presence_state["home"] and \
            self.now_is_between("07:00:00", "22:30:00"):
            # Battery level went from over min level to under min level and the person is home, lets warn!
            self.tts_manager.speak("{}, dags att ladda din mobil. {} ladda din mobil nu!".format(person, person), media_player=self._tts_device)