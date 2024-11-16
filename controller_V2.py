class Controller(object):

    def __init__(self, model):
        self._model = model

    def addShape(self, shapename, shapeid, tlPoint, brPoint, colour):

        self._model.addShape(shapename, shapeid, tlPoint, brPoint, colour)    

    def getShapes(self):
        return self._model.getShapes()
    
    def saveDrawing(self):
        self._model.saveDrawing()

    def loadDrawing(self):
        self._model.loadDrawing()
