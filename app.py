import os
from services import extract_data_from_pdf
# # Replace 'your_folder_path' with the path to the folder containing your PDF bills
def main():
    folder_path = './pdffiles'
    # Iterate over each PDF file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            extract_data_from_pdf(pdf_path)

if __name__ == '__main__':
    main()