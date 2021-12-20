
class encapSub:
    def __init__(self):
        self._protectedVar = 'Ham'
        self.__privateVar = 'Rye'

    def getBread(self):
        print(self.__privateVar)

    def getMeat(self):
        print(self._protectedVar)

    def chgMeat(self, meat):
        self._protectedVar = meat

    def chgBrd(self, bread):    
        self.__privateVar = bread

sandwich = encapSub()

sandwich.getMeat()
sandwich.getBread()

sandwich.chgBrd('wheat')
sandwich.chgMeat('Turkey')

sandwich.getMeat()
sandwich.getBread()

