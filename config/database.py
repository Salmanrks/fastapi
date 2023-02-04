from pymongo import MongoClient


client = MongoClient("mongodb+srv://salman:200926@cluster0.h8acwxi.mongodb.net/?retryWrites=true&w=majority")

db = client.test

collection_name = db["todos_app"]