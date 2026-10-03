# IMPORTANDO MODULOS
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from app.schemas.produto import ProdutoBase

# VALIDAÇÃO VENDAS
class VendaBase(BaseModel):
  id: int
  produto_id: int
  produto: ProdutoBase
  quantidade: float
  valor: float
  forma_pagamento: str
  data: date

  model_config = ConfigDict(from_attributes=True)

# VALIDANDO CRIAÇÃO VENDAS
class VendaCreate(BaseModel):
  produto_id: int
  quantidade: float
  valor: float
  forma_pagamento: str
  data: date = Field(default_factory=date.today)