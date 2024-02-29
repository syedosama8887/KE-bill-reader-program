import os
from services import extract_data_from_pdf
from fastapi import FastAPI,File, UploadFile


app = FastAPI()

@app.post('/getpdfdata')
async def get_pdf_data(pdf_file: UploadFile = File(...)):
    # Check if the uploaded file has a .pdf extension
    if not pdf_file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are allowed."}

    # Save the uploaded file to a temporary location
    pdf_path = os.path.join('./pdffiles', pdf_file.filename)
    with open(pdf_path, 'wb') as f:
        f.write(pdf_file.file.read())

    # Extract data from the PDF file
    extracted_data = extract_data_from_pdf(pdf_path)
    # Optionally, you can delete the temporary file after processing
    os.remove(pdf_path)

    return extracted_data
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)
