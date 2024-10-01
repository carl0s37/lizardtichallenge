from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from controllers.gemini_controller import genai, model, format_document_to_json
from controllers.files_controller import delete_tmp_file, write_tmp_file
from controllers.database_controller import document_collection
from schema.documents_schema import list_serial
from bson import ObjectId


app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile):
  if file.content_type != 'application/pdf':
    raise HTTPException(status_code=400, detail="Tipo de arquivo inválido. Apenas PDFs são permitidos")
  await write_tmp_file('tmp/file.pdf', file)
  gen_ai_file = genai.upload_file(path="tmp/file.pdf", display_name="Gemini 1.5 PDF")
  cloud_file = genai.get_file(name=gen_ai_file.name)
  delete_tmp_file('tmp/file.pdf')
  format_document_to_json(cloud_file)
  genai.delete_file(gen_ai_file.name)
  return JSONResponse(status_code=201, content={"message": "O arquivo foi enviado com sucesso!" })

@app.get('/documents')
async def get_documents():
  documents = document_collection.find()
  return list_serial(documents)

@app.post('/chat/{_id}')
async def talk_to_gemini(_id: str, prompt: str ):
  file = document_collection.find_one({'_id': ObjectId(_id)})
  return model.generate_content(f'{prompt}\nEu estou falando sobre esse arquivo: {file}').text