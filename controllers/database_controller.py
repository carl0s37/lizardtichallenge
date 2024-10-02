from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:admin@cluster0.t8ilw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Configuração do Cliente do Banco de Dados MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

def test_connection():
  # Testa se a conexão com o Banco de Dados do MongoDB funcionou
  try:
    client.admin.command('ping')
    print("Conectado com sucesso ao MONGODB!")
  except Exception as e:
    print(e)

# Criação do Banco de Dados de documentos
db = client.document_db

# Criação da coleção de documentos
document_collection = db['document_collection']

