
class encapSub:
    # Sets protected and private variables
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

print(sandwich._protectedVar)   # Works with protected access
sandwich.getBread()

sandwich._protectedVar = 'Turkey'   # Changes protected var. Won't work for private
sandwich.chgBrd('wheat')

print(sandwich._protectedVar)
sandwich.getBread()

print(sandwich._protectedVar)   
print(sandwich.__privateVar)    # Deliberately coded to cause an error

