from random import randint

class Wheel(object):

    def __init__(self):
        self.orientation = randint(0, 360)
        #herover defineres instansen orientation som et tilfældigt tal mellem 0 og 360 da det er så mange grader er i en cirkel

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360
        #herover opdateres definationen af orientationen af hjulet og matematikken bruges til at holde værdien mellem 0 og 360

class Gearbox(object):

    def __init__(self):
        self.wheels = {'frontLeft': Wheel(), 'frontRight': Wheel(), 'rearLeft': Wheel(), 'rearRight':Wheel()}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        #herover defineres en masse instanser :D

    def shiftUp(self):
        if self.currentGear < len(self.gears)-1 and not self.clutchEngaged:
            self.currentGear = self.currentGear + 1
        #herover defineres funktionen shiftUp. Hvor at currentGear får +1, hvis den er mindre end den største i listen gears, og at clutchEngaged er falsk

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged:
            self.currentGear = self.currentGear - 1
        #herover defineres funktionen shiftdown. Hvor at currentgear får -1, hvis den er større end nul og clutchEngaged er falsk

    def rotate(self, revolutions):
        if self.clutchEngaged:
            for wheel in self.wheels:
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear])
        #herover defineres funktionen rotate. Hvor at der kaldes rotate i wheels med revolution*gears som parameter, hvis clutchEngaged er sand

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100
    #her defineres instanserne der bruges i tanken

    def refuel(self):
        self.contents = self.capacity
        #herover defineres refuel som fylder tankens contents op til capacity

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0
        #herover defineres remove som fjerner en uspecificeret amount fra tankens contents og hvis contents kommer under 0 bliver det bare 0

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()
        #herover defineres instanser som bruges i engine

    def updateModel(self, dt):
        if self.theTank.contents > 0:
            #hvis tankens contents er over 0
            self.currentRpm = self.throttlePosition * self.maxRpm
            #hvor hårdt du trykker speederen ned mellem 0 og 1 * maxRpm
            n = self.currentRpm * self.consumptionConstant
            # her defineres instansen n
            self.theTank.remove(n)
            #her kaldes remove() fra Tank med instansen n som parameter
            o = self.currentRpm * (dt / 60)
            #her defineres instansen o
            self.theGearbox.rotate(o)
            #her kaldes rotate() fra gearbox med instansen o fra parameter
        else:
            self.currentRpm = 0
            #ellers er hjulenes rotationer per minut 0

class Car(object):

    def __init__(self):
        self.theEngine = Engine()
        #her defineres instansen the engine som engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)
        #her kaldes på updatemodel fra theEngine med dt som parameter
