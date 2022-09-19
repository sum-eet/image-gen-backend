# from data import question_data1
import shutil  # save img locally
from flask import Flask, request, url_for

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
from pymongo import MongoClient
from flask_pymongo import pymongo
from urllib.request import urlopen
from io import BytesIO
import base64
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
from pymongo import MongoClient
import pymongo


app = Flask(__name__)


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://sumeet:sumeet@cluster0.au8eazh.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']


@app.route('/')
def index():
    return '''
      <form method = "POST" action = "/create" enctype="multipart/form-data">
        <input type="text" name="username" >
        <input type="file" name="profile_image" >
        <input type="submit">
       </form >
    '''


@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']

        # client.save_file(profile_image.filename, profile_image)
        # client.db.users.insert({'username': request.form.get(
        #     'username'), 'profile_image_name': profile_image.filename})

        dbname = get_database()
        collection_name = dbname["user_1_items"]
        item_1 = {
            "_id": "U1IT00001",
            "item_name": "Blender",
            "max_discount": "10%",
            "batch_number": "RR450020FRG",
            "price": 340,
            "category": "kitchen appliance"
        }

        item_2 = {
            "_id": "U1IT00002",
            "item_name": "Egg",
            "category": "food",
            "quantity": 12,
            "price": 36,
            "item_description": "brown country eggs"
        }
        # collection_name.insert_many([item_1, item_2])
        collection_name.insert_one(profile_image)
    return 'Done!'


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    dbname = get_database()
    app.run(debug=True, port=5000)
    # Get the database
    # collection_name = dbname["user_1_items"]
    # item_1 = {
    #     "_id": "U1IT00001",
    #     "item_name": "Blender",
    #     "max_discount": "10%",
    #     "batch_number": "RR450020FRG",
    #     "price": 340,
    #     "category": "kitchen appliance"
    # }

    # item_2 = {
    #     "_id": "U1IT00002",
    #     "item_name": "Egg",
    #     "category": "food",
    #     "quantity": 12,
    #     "price": 36,
    #     "item_description": "brown country eggs"
    # }
    # collection_name.insert_many([item_1, item_2])
