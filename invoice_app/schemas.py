import datetime

from typing import Optional

from pydantic import BaseModel


class InvoiceItemBase(BaseModel):
    units: int
    description: Optional[str] = None
    amount: float


class InvoiceItemCreate(InvoiceItemBase):
    pass


class InvoiceItem(InvoiceItemBase):
    id: int
    invoice_id: int

    class Config:
        orm_mode = True


class InvoiceBase(BaseModel):
    date: datetime.date


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase)
    id: int
    invoice_items: list[InvoiceItem] = []

    class Config:
        orm_mode = True
