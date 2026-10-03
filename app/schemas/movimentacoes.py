# IMPORTANDO MODULOS
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import date

# VALIDAÇÃO MOVIMENTAÇÃO
class MovimentacaoBase(BaseModel):
  id: int
  tipo: str
  produto_id: Optional[int] = None
  quantidade: Optional[float] = None
  valor: float
  descricao: Optional[str] = None
  data: date

  model_config = ConfigDict(from_attributes=True)

# VALIDANDO CRIAÇÃO MOVIMENTAÇÃO
class MovimentacaoCreate(BaseModel):
  tipo: str
  produto_id: Optional[int] = None
  quantidade: Optional[float] = None
  valor: float
  descricao: Optional[str] = None
  data: date = Field(default_factory=date.today)