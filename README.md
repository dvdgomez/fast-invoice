# Overview of fast-invoice:

Fast-invoice is a FastAPI web framework app that utilizes SQLAlchemy ORM.

invoice-app
* database.py
  * SQLAlchemy support is added here
* models.py
  * SQLAlchemy models located here
* schemas.py
  * Pydantic models located here
* crud.py
  * Create, Read, Update, and Delete (CRUD) invoices and invoice items
* main.py
  * Main FastAPI invoice app and path operations

# Setup:

FastAPI Install: 
* requires fastapi and uvicorn[standard] packages
* part of the dependencies in requirements.txt so pip install that file
* python3 -m pip install -r requirements.txt

Docker Install:
* On Ubuntu "sudo apt install docker.io"
* https://docs.docker.com/get-docker/

Docker Build:
* docker build --tag fast-invoice .
* If all goes well, should show in "docker images" along with the base image
* If not, may not to run with elevated privileges
* sudo docker build --tag fast-invoice .

Docker Run:
* To run the docker image and expose the expected port 8000, run the following:
* docker run --publish 8000:8000 fast-invoice
* To run in detached mode
* docker run -d -p 8000:8000 fast-invoice

See requirements.txt for Python packages needed

# How to run:

In the root directory of this repo, run the following:

uvicorn invoice_app.main:app --reload

Should see something like:

"INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)"

Navigate to the following URL, can manually try out GET and POST route
operations on this page:

http://127.0.0.1:8000/docs#/

# SQLite

If SQLite was used, consider using DB Browser for SQLite

Read more here: https://sqlitebrowser.org/
