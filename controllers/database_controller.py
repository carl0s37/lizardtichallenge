from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:admin@cluster0.t8ilw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

def test_connection():
  try:
    client.admin.command('ping')
    print("Conectado com sucesso ao MONGODB!")
  except Exception as e:
    print(e)

db = client.document_db

document_collection = db['document_collection']

