#!/usr/bin/env python
# coding: utf-8

# You need PIL <http://www.pythonware.com/products/pil/> to run this script
# Download unifont.ttf from <http://unifoundry.com/unifont.html> (or use
# any TTF you have)
# Copyright 2011 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
import sys
from image_utils import ImageText
from PIL import Image

from data import question_data1

color = (50, 50, 50)
text = 'Python is a cool programming language. You should learn it. Lauda lassan yeh wo aisa waise! You should learn it. Lauda lassan yeh wo aisa waise!You should learn it. Lauda lassan yeh wo aisa waise!'

Point1 = []
Point2 = []


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        # layout = QVBoxLayout()
        # self.setLayout(layout)

        # self.pix = QPixmap(self.rect().size())
        # self.pix.fill(Qt.white)
        label = QLabel(self)
        self.pix = QPixmap('GajbImage.png')
        label.setPixmap(self.pix)
        self.resize(self.pix.width(), self.pix.height())
        print(self.pix.width(), self.pix.height())

        self.begin, self.destination = QPoint(), QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pix)

        if not self.begin.isNull() and not self.destination.isNull():
            rect = QRect(self.begin, self.destination)
            painter.drawRect(rect.normalized())

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            print('Point 1')
            self.begin = event.pos()
            self.destination = self.begin
            print(f"{event.x()}, {event.y()}")
            Point1.append(event.x())
            Point1.append(event.y())
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            # print('Point 2')
            self.destination = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        print('Point 3')
        if event.button() & Qt.LeftButton:
            rect = QRect(self.begin, self.destination)
            painter = QPainter(self.pix)
            painter.drawRect(rect.normalized())

            self.begin, self.destination = QPoint(), QPoint()
            print(f"{event.x()}, {event.y()}")
            Point2.append(event.x())
            Point2.append(event.y())
            self.update()


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
		QWidget {
			font-size: 30px;
		}
	''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')


# questions_bank = []
# for question in question_data1:
#     question_text = question["text"]
#     questions_bank.append(question_text)


# question_no = 0

# for question in questions_bank:

#     question_no += 1

#     text = str(question)
font = 'Inter.ttf'
img = ImageText(filename_or_size="GajbImage.png")  # 200 = alpha

# img = ImageText((1750, 961), filename_or_size="GajbImage.png")  # 200 = alpha

# write_text_box will split the text in many lines, based on box_width
# `place` can be 'left' (default), 'right', 'center' or 'justify'
# write_text_box will return (box_width, box_calculed_height) so you can
# know the size of the wrote text
img.write_text_box((300, 50), text, box_width=200, font_filename=font,
                   font_size=15, color=color)
# img.write_text_box((300, 125), text, box_width=200, font_filename=font,
#                    font_size=15, color=color, place='right')
# img.write_text_box((300, 200), text, box_width=200, font_filename=font,
#                    font_size=15, color=color, place='center')
# img.write_text_box((300, 275), text, box_width=200, font_filename=font,
#                    font_size=15, color=color, place='justify')

# You don't need to specify text size: can specify max_width or max_height
# and tell write_text to fill the text in this space, so it'll compute font
# size automatically
# write_text will return (width, height) of the wrote text
img.write_text((100, 350), 'test fill', font_filename=font,
               font_size='fill', max_height=150, color=color)

# fill_text_box will attempt to use up all available space in both x and
# y dimensions, where the above example will only stick to one line
textareawidth = Point2[0] - Point1[0]
textareaheight = Point2[1] - Point1[1]

img.fill_text_box((Point1[0], Point1[1]), text, box_width=textareawidth, box_height=textareaheight,
                  font_filename=font)


img.save('image3.png')
background = Image.open("GajbImage.png")
overlay = Image.open("image3.png")

# background = background.convert("RGBA")
# overlay = overlay.convert("RGBA")

# new_img = Image.blend(background, overlay, 1)
# new_img.save("new.png", "PNG")
