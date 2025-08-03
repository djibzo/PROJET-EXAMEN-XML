from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://djibrilf:rhmAtMmw8z1xHJG5@cluster0.f6wb0nc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

commandesFile = "commande.xml"
