from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# Create database tables
# TODO: Recommended to use Alembic to initialize database tables and 
# for "migrations". Read more here: https://alembic.sqlalchemy.org
models.Base.metadata.create_all(bind=engine)

# App name called with uvicorn ie invoice_app.main:app
app = FastAPI()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/invoices/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db=db, invoice=invoice)


@app.get("/invoices/", response_model=list[schemas.Invoice])
def read_invoices(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    invoices = crud.get_invoices(db, offset=offset, limit=limit)
    if invoices is None:
        raise HTTPException(status_code=404, detail="No invoices found")
    return invoices


@app.get("/invoices/{invoice_id}", response_model=schemas.Invoice)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@app.post("/invoices/{invoice_id}/invoice_items", response_model=scheams.InvoiceItem)
def create_invoice_item(
    invoice_id: int, item: schemas.InvoiceItemCreate, db: Session = Depends(get_db)):
):
    return crud.create_invoice_item(db=db, item=item, invoice_id=invoice_id)


@app.get("/invoice_items/", response_model=list[schemas.InvoiceItem])
def read_invoice_items(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_invoice_items(db, offset=offset, limit=limit)
    if items is None:
        raise HTTPException(status_code=404, detail="No invoice items found")
    return items

