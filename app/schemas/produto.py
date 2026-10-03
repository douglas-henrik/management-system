# IMPORTANDO MODULOS
from typing import Optional
from pydantic import BaseModel, ConfigDict

# VALIDANDO PRODUTO
class ProdutoBase(BaseModel):
  id: int
  nome: str
  categoria: Optional[str] = None
  unidade_gerenciamento: str
  ativo: bool

  model_config = ConfigDict(from_attributes=True)

# VALIDANDO CRIAÇÃO DE PRODUTO
class ProdutoCreate(BaseModel):
  nome: str
  categoria: Optional[str] = None
  unidade_gerenciamento: str
  ativo: bool = True