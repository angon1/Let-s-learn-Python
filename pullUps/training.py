class Excercise:

    def __init__(self, name):
        self.name = name

    def printuj():
        print("%s \n %s" % (self.name))

    def setName(name):
        self.name = name

    def getName(self):
        return self.name

class ExcerciseSet(Excercise):
    def __init__(self, name, reps):
        self.name = name
        self.reps = reps
    def getReps(self):
        return self.reps

#break time - przerwa w serii. Jelsi jest wiecej cwiczen niz jedno, to przerwa jest po wykonaniu powtorzen kazdego z cwiczen
class ExcerciseBlock:
    def __init__(self, repsNumber, breakTime):
        self.repsNumber = repsNumber
        self.breakTime = breakTime
        self.excercise = []

    def addExcercise(self, name, reps):
        self.excercie.append(ExcerciseSet(name, reps))
   
        





class Training:
    name = "Training name"
    blocks = []





