# Electricity Bill PDF Reader

A FastAPI endpoint that accepts a PDF upload and extracts fields using the existing PDF parsing service.

## Overview

`POST /getpdfdata` takes a multipart `pdf_file`, checks its filename extension, writes a temporary file, and passes the PDF to `services/DataExtractionService.py` for extraction.

## Tech stack

Python, FastAPI, Uvicorn, and PyPDF2. Additional exploratory scripts in `services/` use other libraries and are not required for the main endpoint.

## Structure

- `app.py` — upload endpoint.
- `services/DataExtractionService.py` — extraction implementation.
- `requirements.txt` — dependencies for the main app.
- `pdffiles/` — currently tracked sample bill; publication rights and personal-data safety must be checked.

## Installation and usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

On Windows activate with `.venv\Scripts\activate`. FastAPI's interface is at `http://127.0.0.1:8000/docs`. Upload a PDF that you are authorized to process with `POST /getpdfdata` and multipart form field `pdf_file`.

## Limitations

The route checks the file extension rather than validating PDF contents. It uses a temporary file and currently has incomplete exception handling; verify with your own non-sensitive PDF before relying on its output. No environment variables are read by the main app. Do not publish real customer bills as demo material.
