from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)

    invoiceItem = relationship("InvoiceItem", back_populates="invoice")


class InvoiceItem(Base):
    __tablename__ = "invoiceItem"

    id = Column(Integer, primary_key=True, index=True)
    units = Column(Integer)
    description = Column(String)
    amount = Column(Numeric)
    invoice_id = Column(Integer, ForeignKey("invoice.id"))

    invoice = relationship("Invoice", back_populates="invoiceItem")
