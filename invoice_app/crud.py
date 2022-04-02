import datetime

from sqlalchemy.orm import Session

from . import models, schemas


def get_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()


def get_invoice_by_date(db: Session, date: datetime.date):
    return db.query(models.Invoice).filter(models.Invoice.date == date).first() 


def get_invoices(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Invoice).offset(offset).limit(limit).all()


def create_invoice():


def get_invoice_items(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.InvoiceItem).offset(offset).limit(limit).all()


def create_invoice_item():


