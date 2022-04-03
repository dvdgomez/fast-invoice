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
* docker build -t fast-invoice .
* If all goes well, should show in "docker images" along with the base image
* If not, may have to run with elevated privileges
* sudo docker build -t fast-invoice .

Docker Run:
* To run the docker image and expose the expected port 80, run the following:
* docker run -p 80:80 fast-invoice
* To run in detached mode with a named container
* docker run -d --name fast-invoice-ctn -p 80:80 fast-invoice
* Don't need instructions below, simply navigate to http://127.0.0.1/docs#

See requirements.txt for Python packages needed

# How to run (without Docker):

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

# Testing

Recommended to use pytest for testing, see more here: https://docs.pytest.org/en/7.1.x/getting-started.html#get-started

# Lint

PEP8 lint tool used pycodestyle, see more here: https://pypi.org/project/pycodestyle/
