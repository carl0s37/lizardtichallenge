from pydantic import BaseModel
from decimal import Decimal

class Empresa(BaseModel):
    razao_social: str
    cnpj: str

class ObjetoDoContrato(BaseModel):
    data_inicial: str
    data_final: str
    descricao: str

class DetalhesPagamento(BaseModel):
    valor_total: Decimal
    parcelas: int

class DetalhesFinanceiros(BaseModel):
    lucro_operacional: Decimal
    resultado_liquido: Decimal

class Contrato(BaseModel):
    empresa_contratante: Empresa
    empresa_contratada: Empresa
    objeto_do_contrato: ObjetoDoContrato
    detalhes_pagamento: DetalhesPagamento
    detalhes_financeiros: DetalhesFinanceiros