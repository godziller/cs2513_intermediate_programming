#TODO: add overarching app that representes full configuration of classes used.

from model import Model
from controller import Controller
from view import View

if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    view = View(controller)