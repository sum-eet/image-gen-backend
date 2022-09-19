# from data import question_data1
import shutil  # save img locally
from flask import Flask, request

import requests
import json
from datetime import date
from PIL import Image, ImageDraw, ImageFont
from image_utils import ImageText

import urllib.request
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
import sys
from image_utils import ImageText
from PIL import Image
import urllib
from urllib.request import urlopen
from io import BytesIO


app = Flask(__name__)


# @app.route("/result", methods=["POST", "GET"])
# def result():
#     # return {"API": "Response Positive"}
#     # output = request.get_json()

#     # if len(output.keys()) < 2:
#     #     return{"status": "bad response"}
#     # num1 = str(output['num1'])
#     # image = Image.open("GajbImage.png")
#     # draw = ImageDraw.Draw(image)
#     # font = ImageFont.truetype('Inter.ttf', size=50)
#     # content = str(num1)

#     # color = 'rgb(0,0,0)'
#     # draw.text((440, 240), content, color, font=font)

#     # return image.show("testtoday22.png")

#     color = (50, 50, 50)
#     # text = 'Python is a cool programming language. You should learn it. Lauda lassan yeh wo aisa waise!'

#     questions_data1 = request.get_json()
#     questions_bank = []
#     for question in question_data1:
#         question_text = question["text"]
#         questions_bank.append(question_text)

#     question_no = 0

#     for question in questions_bank:

#         question_no += 1

#         text = str(question)
#         font = 'Inter.ttf'
#         img = ImageText((800, 600), background=(
#             255, 255, 255, 200))  # 200 = alpha

#         # write_text_box will split the text in many lines, based on box_width
#         # `place` can be 'left' (default), 'right', 'center' or 'justify'
#         # write_text_box will return (box_width, box_calculed_height) so you can
#         # know the size of the wrote text
#         img.write_text_box((300, 50), text, box_width=200, font_filename=font,
#                            font_size=15, color=color)
#         img.write_text_box((300, 125), text, box_width=200, font_filename=font,
#                            font_size=15, color=color, place='right')
#         img.write_text_box((300, 200), text, box_width=200, font_filename=font,
#                            font_size=15, color=color, place='center')
#         img.write_text_box((300, 275), text, box_width=200, font_filename=font,
#                            font_size=15, color=color, place='justify')

#         # You don't need to specify text size: can specify max_width or max_height
#         # and tell write_text to fill the text in this space, so it'll compute font
#         # size automatically
#         # write_text will return (width, height) of the wrote text
#         img.write_text((100, 350), 'test fill', font_filename=font,
#                        font_size='fill', max_height=150, color=color)

#         # fill_text_box will attempt to use up all available space in both x and
#         # y dimensions, where the above example will only stick to one line
#         img.fill_text_box((100, 100), text, box_width=600, box_height=400,
#                           font_filename=font)

#         img.save(f'dhawalsample_{question_no}.png')


# if __name__ == '__main__':
#     app.run(debug=True, port=2000)
# url = input('enter url')
# url = 'https://i.pinimg.com/736x/30/3a/0e/303a0eb9215fff7212ca3261920c09da.jpg'

# url = 'https://lh3.googleusercontent.com/KtIGnNDtlT9JZsGUfm5BygB6CzIOQYJGfvao-DKNv7PhOXPWcNDs-O3CBeTlWFpgRjGeodq_XJdKzKmYeryPFZZMTU8uvs7YUIpuzL0W6i91lNh8AF0YEXItJyh3=e365-rj-l80-w364'
# file_name = 'ImagefromURL.png'  # prompt user for file_name

# res = requests.get(url, stream=True)

# if res.status_code == 200:
#     with open(file_name, 'wb') as f:
#         shutil.copyfileobj(res.raw, f)
#     print('Image sucessfully Downloaded: ', file_name)
# else:
#     print('Image Couldn\'t be retrieved')

# Point1 = []
# Point2 = []


# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.window_width, self.window_height = 1200, 800
#         self.setMinimumSize(self.window_width, self.window_height)

#         # layout = QVBoxLayout()
#         # self.setLayout(layout)

#         # self.pix = QPixmap(self.rect().size())
#         # self.pix.fill(Qt.white)
#         label = QLabel(self)
#         self.pix = QPixmap('ImagefromURL.png')
#         label.setPixmap(self.pix)
#         self.resize(self.pix.width(), self.pix.height())
#         print(self.pix.width(), self.pix.height())

#         self.begin, self.destination = QPoint(), QPoint()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawPixmap(QPoint(), self.pix)

#         if not self.begin.isNull() and not self.destination.isNull():
#             rect = QRect(self.begin, self.destination)
#             painter.drawRect(rect.normalized())

#     def mousePressEvent(self, event):
#         if event.buttons() & Qt.LeftButton:
#             print('Point 1')
#             self.begin = event.pos()
#             self.destination = self.begin
#             print(f"{event.x()}, {event.y()}")
#             Point1.append(event.x())
#             Point1.append(event.y())
#             self.update()

#     def mouseMoveEvent(self, event):
#         if event.buttons() & Qt.LeftButton:
#             # print('Point 2')
#             self.destination = event.pos()
#             self.update()

#     def mouseReleaseEvent(self, event):
#         print('Point 3')
#         if event.button() & Qt.LeftButton:
#             rect = QRect(self.begin, self.destination)
#             painter = QPainter(self.pix)
#             painter.drawRect(rect.normalized())

#             self.begin, self.destination = QPoint(), QPoint()
#             print(f"{event.x()}, {event.y()}")
#             Point2.append(event.x())
#             Point2.append(event.y())
#             self.update()


@app.route("/result", methods=["POST", "GET"])  # "POST",
def result():
    # dataaa = request.get_json()
    # print(dataaa['text'])
    # return {"API": "Response Positive"}
    # output = request.get_json()

    # if len(output.keys()) < 2:
    #     return{"status": "bad response"}
    # num1 = str(output['num1'])
    # image = Image.open("GajbImage.png")
    # draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype('Inter.ttf', size=50)
    # text = str(num1)
    # return {
    #     'name': 'Hello Worlder'
    # }
    import requests
    # color = 'rgb(0,0,0)'
    # draw.text((440, 240), content, color, font=font)

    # return image.show("testtoday22.png")
    # url = "https://i.imgur.com/QZXIwE2.jpeg"
    # url_response = urllib.response.urlopen(url)
    question_data1 = request.get_json()['text']
    # question_data1 = request.get_json()
    # url = question_data1["link"]
    url = request.get_json()["link"]
    print(url)
    print(request.get_json()["rest"])
    points = request.get_json()["rest"]

    questions_bank = []
    for question in question_data1:
        question_text = question
        questions_bank.append(question_text)

    # url = request.get_json()
    # url = url[0]["link"]
    # print(url)
    file_name = 'ImagefromURL.png'  # prompt user for file_name

    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', file_name)
    else:
        print('Image Couldn\'t be retrieved')

    color = (0, 0, 0)
    # text = 'Python is a cool programming language. You should learn it. Lauda lassan yeh wo aisa waise! You should learn it. Lauda lassan yeh wo aisa waise!You should learn it. Lauda lassan yeh wo aisa waise!'

    Point1 = []
    Point2 = []
    Point1.append(points[0])
    Point1.append(points[1])
    Point2.append(points[2])
    Point2.append(points[3])

    # class MyApp(QWidget):
    #     def __init__(self):
    #         super().__init__()
    #         self.window_width, self.window_height = 1200, 800
    #         self.setMinimumSize(self.window_width, self.window_height)

    #         # layout = QVBoxLayout()
    #         # self.setLayout(layout)

    #         # self.pix = QPixmap(self.rect().size())
    #         # self.pix.fill(Qt.white)
    #         label = QLabel(self)
    #         self.pix = QPixmap('ImagefromURL.png')
    #         label.setPixmap(self.pix)
    #         self.resize(self.pix.width(), self.pix.height())
    #         print(self.pix.width(), self.pix.height())

    #         self.begin, self.destination = QPoint(), QPoint()

    #     def paintEvent(self, event):
    #         painter = QPainter(self)
    #         painter.drawPixmap(QPoint(), self.pix)

    #         if not self.begin.isNull() and not self.destination.isNull():
    #             rect = QRect(self.begin, self.destination)
    #             painter.drawRect(rect.normalized())

    #     def mousePressEvent(self, event):
    #         if event.buttons() & Qt.LeftButton:
    #             print('Point 1')
    #             self.begin = event.pos()
    #             self.destination = self.begin
    #             print(f"{event.x()}, {event.y()}")
    #             Point1.append(event.x())
    #             Point1.append(event.y())
    #             self.update()

    #     def mouseMoveEvent(self, event):
    #         if event.buttons() & Qt.LeftButton:
    #             # print('Point 2')
    #             self.destination = event.pos()
    #             self.update()

    #     def mouseReleaseEvent(self, event):
    #         print('Point 3')
    #         if event.button() & Qt.LeftButton:
    #             rect = QRect(self.begin, self.destination)
    #             painter = QPainter(self.pix)
    #             painter.drawRect(rect.normalized())

    #             self.begin, self.destination = QPoint(), QPoint()
    #             print(f"{event.x()}, {event.y()}")
    #             Point2.append(event.x())
    #             Point2.append(event.y())
    #             self.update()

    #  if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # print(request.form['text'])
    # print(request.form['image'])

    ####
    # app = QApplication(sys.argv)
    # app.setStyleSheet('''
    #         QWidget {
    #             font-size: 30px;
    #         }
    #     ''')

    # myApp = MyApp()
    # myApp.show()

    # try:
    #     sys.exit(app.exec_())
    # except SystemExit:
    #     print('Closing Window...')

    #####

    # if __name__ == '__main__':
    #     # don't auto scale when drag app to a different monitor.
    #     # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    #     # print(request.form['text'])
    #     # print(request.form['image'])
    #     app = QApplication(sys.argv)
    #     app.setStyleSheet('''
    #         QWidget {
    #             font-size: 30px;
    #         }
    #     ''')

    #     myApp = MyApp()
    #     myApp.show()

    #     try:
    #         sys.exit(app.exec_())
    #     except SystemExit:
    #         print('Closing Window...')

    # question_data1 = request.get_json()
    # # question_data1 = request.get_json()
    # url_12 = question_data1["link"]
    # print(url_12)

    # questions_bank = []
    # for question in question_data1:
    #     question_text = question["text"]
    #     questions_bank.append(question_text)

    question_no = 0

    # img = "https://i.imgur.com/QZXIwE2.jpeg"
    # urllib.request.urlretrieve("https://i.imgur.com/QZXIwE2.jpeg", “gfg.jpeg”)

    # img = Image.open(“file_name”)

    # urllib.request.urlretrieve(
    #     'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
    #     "gfg.png")

    # response = requests.get(
    #     'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png')
    # img = Image.open(BytesIO(response.content))
    import requests  # request img from web

    # prompt user for img url

    for question in questions_bank:

        question_no += 1
        nothing = str(question)
        text = nothing
        font = 'Inter.ttf'
        img = ImageText(filename_or_size='ImagefromURL.png')  # 200 = alpha

        # img = ImageText((1750, 961), filename_or_size="StoryTemplate.png")  # 200 = alpha

        # write_text_box will split the text in many lines, based on box_width
        # `place` can be 'left' (default), 'right', 'center' or 'justify'
        # write_text_box will return (box_width, box_calculed_height) so you can
        # know the size of the wrote text
        # img.write_text_box((300, 50), text, box_width=200, font_filename=font,
        #                    font_size=15, color=color)
        # img.write_text_box((300, 125), text, box_width=200, font_filename=font,
        #                    font_size=15, color=color, place='right')
        img.write_text_box((300, 200), text, box_width=200, font_filename=font,
                           font_size=15, color=color, place='center')
        # img.write_text_box((300, 275), text, box_width=200, font_filename=font,
        #                    font_size=15, color=color, place='justify')

        # You don't need to specify text size: can specify max_width or max_height
        # and tell write_text to fill the text in this space, so it'll compute font
        # size automatically
        # write_text will return (width, height) of the wrote text
        img.write_text((100, 350),  'test fill', font_filename=font,
                       font_size='fill', max_height=150, color=color)

        # fill_text_box will attempt to use up all available space in both x and
        # y dimensions, where the above example will only stick to one line
        textareawidth = Point2[0] - Point1[0]
        textareaheight = Point2[1] - Point1[1]

        img.fill_text_box((Point1[0], Point1[1]), text, box_width=textareawidth, box_height=textareaheight,
                          font_filename=font, place='center')

        img.save(f'image6_{question_no}.png')
        # background = Image.open("GajbImage.png")
        # overlay = Image.open("image3.png")

        #     color = (50, 50, 50)
        #     # text = 'Python is a cool programming language. You should learn it. Lauda lassan yeh wo aisa waise!'

        #     questions_data1 = request.get_json()
        #     questions_bank = []
        #     for question in question_data1:
        #         question_text = question["text"]
        #         questions_bank.append(question_text)

        #     question_no = 0

        #     for question in questions_bank:

        #         question_no += 1

        #         text = str(question)
        #         font = 'Inter.ttf'
        #         img = ImageText((800, 600), background=(
        #             255, 255, 255, 200))  # 200 = alpha

        #         # write_text_box will split the text in many lines, based on box_width
        #         # `place` can be 'left' (default), 'right', 'center' or 'justify'
        #         # write_text_box will return (box_width, box_calculed_height) so you can
        #         # know the size of the wrote text
        #         img.write_text_box((300, 50), text, box_width=200, font_filename=font,
        #                         font_size=15, color=color)
        #         img.write_text_box((300, 125), text, box_width=200, font_filename=font,
        #                         font_size=15, color=color, place='right')
        #         img.write_text_box((300, 200), text, box_width=200, font_filename=font,
        #                         font_size=15, color=color, place='center')
        #         img.write_text_box((300, 275), text, box_width=200, font_filename=font,
        #                         font_size=15, color=color, place='justify')

        #         # You don't need to specify text size: can specify max_width or max_height
        #         # and tell write_text to fill the text in this space, so it'll compute font
        #         # size automatically
        #         # write_text will return (width, height) of the wrote text
        #         img.write_text((100, 350), 'test fill', font_filename=font,
        #                     font_size='fill', max_height=150, color=color)

        #         # fill_text_box will attempt to use up all available space in both x and
        #         # y dimensions, where the above example will only stick to one line
        #         img.fill_text_box((100, 100), text, box_width=600, box_height=400,
        #                         font_filename=font)

        #         img.save(f'dhawalsample_{question_no}.png')


if __name__ == '__main__':
    app.run(debug=True, port=2000)
