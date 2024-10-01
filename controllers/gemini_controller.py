import google.generativeai as genai
import json
from fastapi import File
from controllers.database_controller import document_collection
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key="AIzaSyCwQ0XZXKk03KbIYatKDjY7qMZYeB207cs")
model_name = 'gemini-1.5-flash'
safety_settings={
  HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
  HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}
config = {
  "temperature": 0.6,
  "top_k": 0,
  "top_p": 0.95,
  "max_output_tokens": 1000
}

model = genai.GenerativeModel(
  model_name,
  safety_settings,
  config
)

def response_genai_file(file, prompt):
  response = model.generate_content(f'{prompt}\nUse esse arquivo como base: {file}')
  return response.text

def send_genai_file(file_path: str, file_name: str):
  return genai.upload_file(path=file_path, display_name=file_name)

def format_document_to_json(file: File):
  json_formatting_prompt = """
    Me retorne os dados desse documento
    Use esse JSON schema:

    {
  "empresa_contratante": {
    "razao_social": "Empresa Contratante LTDA",
    "cnpj": "12.345.678/0001-90"
  },
  "empresa_contratada": {
    "razao_social": "Empresa Contratada LTDA",
    "cnpj": "98.765.432/0001-01"
  },
  "objeto_do_contrato": {
    "data_inicial": "2024-01-01",
    "data_final": "2025-01-01",
    "descricao": "Prestação de serviços"
  },
  "detalhes_pagamento": {
    "valor_total": 1000000.00,
    "parcelas": 5
  },
  "detalhes_financeiros": {
    "lucro_operacional": 500000.00,
    "resultado_liquido": 450000.00
  }
}

  """
  response = model.generate_content([file, json_formatting_prompt])
  text_length = len(response.text)
  data = json.loads(response.text[8:text_length-4])
  document_collection.insert_one(data)
  return 
