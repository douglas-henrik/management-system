# IMPORTANDO MODULOS
from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.produto import ProdutoBase

# VALIDAÇÃO DE COMPRA
class CompraBase(BaseModel):
  id: int
  fornecedor: Optional[str] = None
  quantidade: float
  valor: float
  data: date
  produto_id: int
  produto: ProdutoBase

  model_config = ConfigDict(from_attributes=True)

# VALIDANDO CADASTRO DE COMPRA
class CompraCreate(BaseModel):
  fornecedor: Optional[str] = None
  quantidade: float
  valor: float
  data: date = Field(default_factory=date.today)
  produto_id: int