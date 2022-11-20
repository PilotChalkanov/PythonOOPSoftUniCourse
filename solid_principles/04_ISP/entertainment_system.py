class HDMI_ConnectMixin:
    def connect_to_device_via_hdmi_cable(self, device):
        return f'Connected {self} to {device} via HDMI'

class RCA_ConnectMixin:
    def connect_to_device_via_rca_cable(self, device):
        return f'Connected {self} to {device} via RCA'

class Ethernet_ConnectMixin:
    def connect_to_device_via_ethernet_cable(self, device):
        return f'Connected {self} to {device} via Ethernet'

class PowerOuletMixin:
    def connect_device_to_power_outlet(self,device):
        return f'Connected {device} via powerCable'







class Television(RCA_ConnectMixin,HDMI_ConnectMixin,PowerOuletMixin):
    def connect_to_dvd(self, dvd_player):
        return self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMI_ConnectMixin,PowerOuletMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class GameConsole(HDMI_ConnectMixin,Ethernet_ConnectMixin,PowerOuletMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        return self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class Router(Ethernet_ConnectMixin,PowerOuletMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)

tv = Television()
gc = GameConsole()
router = Router()
dvd = DVDPlayer()
tv.plug_in_power()
print(tv.connect_to_dvd(dvd))
print(router.connect_device_to_power_outlet(router))