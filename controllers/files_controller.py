from os import path, remove
from fastapi import UploadFile

# Deleta o arquivo local
def delete_tmp_file(file_path: str):
  # Testa se o arquivo existe
  if path.exists(file_path):
    # Se o arquivo existir ele é deletado
    remove(file_path)
  return

# Salva o arquivo recebido no front-end em um diretório local
async def write_tmp_file(file_path: str, file: UploadFile):
  with open(file_path, "wb") as f:
    f.write(await file.read())
  return