from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict

class FilmBase(BaseModel):
    kode: Optional[str]
    judul: Optional[str]
    pemain_utama: Optional[str]
    jenis: Optional[str]
    ket: Optional[str]
    aktif: Optional[bool]
    lastupdate: Optional[datetime]
    share_profit: Optional[Decimal]

class FilmCreate(FilmBase):
    pass

class FilmUpdate(FilmBase):
    pass

class FilmOut(FilmBase):
    rowid: int

    # NEW for Pydantic v2:
    model_config = ConfigDict(from_attributes=True)
