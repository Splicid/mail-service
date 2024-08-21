from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import os

db_doc = [
    {
        "email": "user@example.com",
        "firstName": "John",
        "lastName": "Doe",
        "subscribed": True,
        "preferences": {
        "frequency": "weekly",
        "topics": ["tech", "news"]
        },
        "createdAt": datetime.now(),
        "updatedAt": datetime.now()
   }
]


def initilize():
    uri = f"mongodb+srv://luis1abreu11:{os.getenv("DB-PASSWORD")}@cluster0.f4werh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    mydb = client["mailing"] 

    #Checks if collection mailing-data already exists if not, create it.
    if "mailing-data" in mydb.list_collection_names():
        print("db already created")
    else:
        try:
            collection = mydb.create_collection("mailing-data")
            collection.insert_one(db_doc)
        except Exception as inste:
            print(inste)


def user_account():
    pass


