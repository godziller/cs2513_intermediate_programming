from person import Person

class Engineer(Person):
    def __init__(self, name, job, salary, forte):
        super().__init__( name, job, salary)
        self._forte = forte
        
    def getForte(self):
        return self._forte
    
    def setForte(self, forte):
        self._forte = forte
        
    project = property(getForte, setForte)
        
    def __str__(self):
        return ("%s who specializes in %s" % (super().__str__(), self._forte))
    
if __name__ == "__main__":
    maxwell = Engineer("Maxwell", "Engineer", 190000, "Electronics")
    print(maxwell)

    oswald = Engineer("Oswald", "Engineer", 160000, "Welding")
    print(oswald)