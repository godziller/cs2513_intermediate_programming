from person import Person

class Manager(Person):
    def __init__(self, name, job, salary, project):
        super().__init__( name, job, salary)
        self._project = project
        
    def getProject(self):
        return self._project
    
    def setProject(self, project):
        self._project = project
        
    project = property(getProject, setProject)
        
    def __str__(self):
        return ("%s with job %s" % (super().__str__(), self._project))
    
if __name__ == "__main__":
    luca = Manager("Luca", "Manger", 120000, "The Big Job")
    print(luca)
    luca.givePayRaise(10)
    print(luca)
    print(luca.project)
