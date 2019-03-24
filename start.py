import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
import main_gui
import ai.predict as pred
from PIL import Image
import numpy as np
from skimage import io, transform, util


class myGui(QtWidgets.QMainWindow, main_gui.Ui_MainWindow):
    new_img = Image.open(os.path.join(os.getcwd(), "assets/image_to_predict.jpeg"))

    def __init__(self, parent=None):
        super(myGui, self).__init__(parent)
        self.setupUi(self)
        self.img_open.clicked.connect(self.openimg)
        self.img_predict.clicked.connect(self.predict)

    def openimg(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()")
        new_img = Image.open(file_name)
        width, height = new_img.size
        new_img.save(os.path.join(os.getcwd(), "assets/image_to_predict.jpeg"))
        pix_map = QtGui.QPixmap(os.path.join(os.getcwd(), "assets/image_to_predict.jpeg"))
        pix_map = pix_map.scaled(500, height, QtCore.Qt.KeepAspectRatio)
        self.img_in.setPixmap(pix_map)
        self.img_in.show()
        # return new_img

    def save_to_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()")
        self.new_img.save(file_name, 'jpeg')
        # self.working_img = Image.open(file_name)

    def predict(self):
        pred.input_image()
        pix_map = QtGui.QPixmap("assets/predict_graph.jpeg")
        pix_map = pix_map.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        self.img_predict_out.setPixmap(pix_map)
        self.img_predict_out.show()
        pix_map = QtGui.QPixmap("assets/grey_img_out.jpeg")
        pix_map = pix_map.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        self.img_grey.setPixmap(pix_map)
        self.img_grey.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([sys.argv])
    window = myGui()
    window.show()
    sys.exit(app.exec_())

