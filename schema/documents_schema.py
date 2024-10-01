from typing import List
from models.document_models import Contrato
def individual_serializer(document: dict) -> dict:
    return {
        '_id': str(document['_id']),
        'empresa_contratante': {
            'razao_social': document['empresa_contratante']['razao_social'],
            'cnpj': document['empresa_contratante']['cnpj']
        },
        'empresa_contratada': {
            'razao_social': document['empresa_contratada']['razao_social'],
            'cnpj': document['empresa_contratada']['cnpj']
        },
        'objeto_do_contrato': {
            'data_inicial': document['objeto_do_contrato']['data_inicial'],
            'data_final': document['objeto_do_contrato']['data_final'],
            'descricao': document['objeto_do_contrato']['descricao']
        },
        'detalhes_pagamento': {
            'valor_total': document['detalhes_pagamento']['valor_total'],
            'parcelas': document['detalhes_pagamento']['parcelas']
        },
        'detalhes_financeiros': {
            'lucro_operacional': document['detalhes_financeiros']['lucro_operacional'],
            'resultado_liquido': document['detalhes_financeiros']['resultado_liquido']
        }
    }
def list_serial(documents) -> List[Contrato]:
  return[individual_serializer(document) for document in documents]