from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from .database import Base

class Film(Base):
    __tablename__ = "FILM"

    rowid = Column("ROWID", Integer, primary_key=True, index=True)
    kode = Column("KODE", String(10), nullable=True)
    judul = Column("JUDUL", String(30), nullable=True)
    pemain_utama = Column("PEMAIN_UTAMA", String(30), nullable=True)
    jenis = Column("JENIS", String(8), nullable=True)
    ket = Column("KET", String(50), nullable=True)
    aktif = Column("AKTIF", Boolean, nullable=True)
    lastupdate = Column("LASTUPDATE", DateTime, nullable=True)
    share_profit = Column("SHARE_PROFIT", Numeric(10, 4), nullable=True)
