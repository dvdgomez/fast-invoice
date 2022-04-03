import datetime

from sqlalchemy.orm import Session

from . import models, schemas


def get_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()


def get_invoice_by_date(db: Session, date: datetime.date):
    return db.query(models.Invoice).filter(models.Invoice.date == date).first()


def get_invoices(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Invoice).offset(offset).limit(limit).all()


def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    # create SQLAlchemy Invoice model instance
    db_invoice = models.Invoice(date=invoice.date)
    # add to database session
    db.add(db_invoice)
    # commit changes to database to save
    db.commit()
    # refresh database instance
    db.refresh(db_invoice)
    return db_invoice


def get_invoice_items(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.InvoiceItem).offset(offset).limit(limit).all()


def create_invoice_item(db: Session, item: schemas.InvoiceItemCreate, invoice_id: int):
    # create SQLAlchemy InvoiceItem model instance
    db_invoice_item = models.InvoiceItem(**item.dict(), invoice_id=invoice_id)
    # add to database session
    db.add(db_invoice_item)
    # commit changes to database to save
    db.commit()
    # refresh database instance
    db.refresh(db_invoice_item)
    return db_invoice_item
