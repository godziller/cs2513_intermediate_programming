class Model(object):
    pass

    # TODO: Add cxtr
    def __init__(self):
        self._shapesDict = {}
        self._shapecount = 0

    def addShape(self, shapename, shapeId, tlPoint, brPoint, colour):
        shapeId = shapename + str(self._shapecount)
        self._shapecount += 1

        shape = ''
        if shapename == "circle":
            shape = Circle(shapename, shapeId, tlPoint, brPoint, colour)
            #TODO: remember to add a default shape subclass here
        self._shapesDict[shapeId] = shape

    def deleteShape(self, shapeId):
        if shapeId in self._shapesDict:
            del self._shapesDict[shapeId]

    def getShape(self, shapeId):

        return self._shapesDict(shapeId)

    def getShape(self):
        return self._shapesDict.values()

class Point(object):

    def __init__(self, xval, yval):

        self._x = xval
        self._y = yval

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, xval):
        self._x = xval


    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y

class Shape(object):

    def __init__(self, shapename, shapeId, tlPoint, brPoint, colour):

        self._shapename = shapename
        self._shapeId = shapeId
        self._tlPoint = tlPoint
        self._brPoint = brPoint
        self._colour = colour

    @property
    def shapename(self):

        return self._shapename
    
    @property
    def tlPoint(self):

        return self._tlPoint
    
    @tlPoint.setter
    def tlPoint(self, newPoint):
        self._tlPoint = newPoint

    @property
    def brPoint(self):

        return self._brPoint
    
    @brPoint.setter
    def brPoint(self, newPoint):
        self._brPoint = newPoint

    @property
    def colour(self):

        return self._colour
    
    @colour.setter
    def colour(self, newColour):
        self._colour = newColour 

class Circle(Shape):

    def __init__(self, shapename, shapeid, tlPoint, brPoint, colour):

        super().__init__(shapename, shapeid, tlPoint, brPoint, colour)   