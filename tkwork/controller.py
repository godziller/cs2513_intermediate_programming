class Controller(object):
    def __init__(self, model):
        self._model = model

    def addShape(self, shapename, shapeid, tlPoint, brPoint, colour):
        self._model.addShape(shapename, shapeid, tlPoint, brPoint, colour)

    def getShapes(self):
        return self.getShapes()
    #TODO: add cxtr - initalize with model instance
    #TODO: addShape(self, shapename, shapeid, tlPoint, brPoint, colour) no return no exceptions - add a new shape to the model
    #TODO: getShapes(self) returns list of shapes no exceptions - returns list of all shapes