import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from db_connection import get_db
from bson import ObjectId
import xml.etree.ElementTree as ET
from pymongo import MongoClient

db = get_db()
collection = db["categories"]
# ------------------ ANALYSE ------------------
def nombre_total_categories():
    total = collection.count_documents({})
    print(f"Nombre total de catégories : {total}")