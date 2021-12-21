from abc import ABC, abstractmethod


class hockeyStick(ABC):

    @abstractmethod
    def stickName(self):
        pass


class Bauer(hockeyStick):

    # overriding abstract method
    def stickName(self):
        print("Our newest stick is called the HyperLite")


class CCM(hockeyStick):

    # overriding abstract method
    def stickName(self):
        print("Our newest stick is called the Trigger 5")


class Warrior(hockeyStick):

    # overriding abstract method
    def stickName(self):
        print("Our newest stick is called the Alpha QRX")


class Sherwood(hockeyStick):

    # overriding abstract method
    def stickName(self):
        print("Our newest stick is called the Rekker")


# Driver code
bauer = Bauer()
bauer.stickName()

ccm = CCM()
ccm.stickName()

warrior = Warrior()
warrior.stickName()

sherwood = Sherwood()
sherwood.stickName()