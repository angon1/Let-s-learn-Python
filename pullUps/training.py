class Excercise:

    def __init__(self, name):
        self.name = name

    def printuj(self):
        print("%s \n %s" % (self.name))

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

class ExcerciseSet(Excercise):
    def __init__(self, name, reps):
        self.name = name
        self.reps = reps

    def getReps(self):
        return self.reps

    def printMe(self):
        print("%s x %d" % (self.name, self.reps))

class ExcerciseBlock:
    def __init__(self, repsNumber, breakTime):
        self.repsNumber = repsNumber
        self.breakTime = breakTime
        self.excercise = []

    def addExcercise(self, name, reps):
        self.excercise.append(ExcerciseSet(name, reps))

    def getRepsNumber(self):
        return self.repsNumber

    def getBreakTime(self):
        return self.breakTime
    
    def getExcercises(self):
        return self.excercise

    def printMe(self):
        print("Powtórzenia bloku: %d\tPrzerwa: %d" % (self.repsNumber, self.breakTime))
        for i in range(len(self.excercise)):
            self.excercise[i].printMe()



class Training:
    def __init__(self):
        self.blocks = []

    def addBlock(self):
        self.repsNumber = int(input("Podaj liczbę powtorzeń bloku cwiczen: \n"))
        self.breakTime = int(input("Podaj czas przerwy między powtórzeniami bloku: \n"))
        self.blocks.append(ExcerciseBlock(self.repsNumber, self.breakTime))
        while 0 == 0:
            self.name = input("Wprowadź nazwe cwiczenia. Jesli nie chcesz dodawac cwiczen do bloku, wpisz 0: \n")
            if "0" == self.name:
                break
            self.reps = int(input("Wprowadź liczbę powtórzeń: "))
            self.blocks[-1].addExcercise(self.name, self.reps)
        print("Blok dodany")


    def printMe(self):
        print("Twój trening")
        for i in range(len(self.blocks)):
            print("Blok %d:" % i)
            self.blocks[0].printMe()

    def printMeVoid():
        return("Twój trening")



# trening = Training()


# trening.addBlock()
# trening.printMe()


    


