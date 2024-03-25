import os
from services import extract_data_from_pdf
from fastapi import FastAPI,File, UploadFile
from tempfile import NamedTemporaryFile
import io
import shutil
app = FastAPI()

@app.post('/getpdfdata')
async def get_pdf_data(pdf_file: UploadFile = File(...)):
    try:
        # Check if the uploaded file has a .pdf extension
        if not pdf_file.filename.lower().endswith(".pdf"):
            return {"error": "Only PDF files are allowed."}
        temp = NamedTemporaryFile(delete=False, suffix='.pdf')
        with open(temp.name, 'wb') as f:
            shutil.copyfileobj(pdf_file.file, f)
        await pdf_file.close()
        temp.close()
        pdf_path = temp.name
        # Extract data from the PDF file
        extracted_data = extract_data_from_pdf(pdf_path)
        return extracted_data
    except Exception as e:
        print(e)
    finally:
        
        # Optionally, you can delete the temporary file after processing
        os.remove(pdf_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)
