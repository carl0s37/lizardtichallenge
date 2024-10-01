from os import path, remove
from fastapi import UploadFile

def delete_tmp_file(file_path: str):
  if path.exists(file_path):
    remove(file_path)
  return

async def write_tmp_file(file_path: str, file: UploadFile):
  with open(file_path, "wb") as f:
    f.write(await file.read())
  return