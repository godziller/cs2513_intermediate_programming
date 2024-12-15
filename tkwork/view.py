from tkinter import Tk, Frame, Button, Canvas
from model import Point

class View(object):

    def __init__(self, controller):

        self._controller = controller

        # Add ability to track button selections
        self._currentShape = ""
        self._currentColour = ""

        root = Tk()
        root.title("Our Brillian Graphics App")
        root.maxsize(930,620)

        button_frame = Frame(root, width=200, height=580)
        button_frame.grid(row=0, column=0, padx=10, pady=10)
        button_frame.grid_propagate(False)

        canvas_frame = Frame(root, width=700, height=600, bg='red')
        canvas_frame.grid(row=0, column=1)
        canvas_frame.grid_propagate(False)

        self._circleButton = Button(button_frame, text="Circle", command=self.circleButtonPressed)
        self._circleButton.pack()

        self._redButton = Button(button_frame, text="Red", command=self.redButtonPressed)
        self._redButton.pack()

        self._canvas = Canvas(canvas_frame, bg="white", width=300, height=300)
        self._canvas.bind("<Button-1>", self.mouseClicked)
        self._canvas.pack()

        root.mainloop()

    def mouseClicked(self, event):
        
        tlPoint = Point(event.x, event.y)
        brPoint = Point(event.x + 20, event.y + 20)

        self._controller.addShape(self._currentShape, '', tlPoint, brPoint, self._currentColour)

        self._canvas.delete('all')
        shapes = self._controller.getShapes()

        for shape in shapes:
            if shape.shapename == 'circle':
                self._canvas.create_oval(shape.tlPoint.x, shape.tlPoint.y, shape.brPoint.x,
                                         shape.brPoint.y, fill=shape.colour)
        # TODO: add handling for new shape

    def circleButtonPressed(self):
        self._currentShape = 'circle'

    def redButtonPressed(self):
        self._currentColour = 'red'
        # TODO: update state of view to know which current colour is selected
