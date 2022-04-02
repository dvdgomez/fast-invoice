from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship

from .database import Base


# Invoice Model
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)

    invoice_items = relationship("InvoiceItem", back_populates="invoice")


# InvoiceItem Model
class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    units = Column(Integer)
    description = Column(String)
    amount = Column(Numeric)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    invoice = relationship("Invoice", back_populates="invoice_items")

