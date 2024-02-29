import re
import PyPDF2
def extract_data_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Assume that the relevant information is in the first page
        first_page = reader.pages[0]
        text = first_page.extract_text()
        # Convert the extracted text into a list
        lines = text.split('\n')
        # Remove lines containing specific patterns
        # Remove lines containing specific keys
        filtered_lines = [line for line in lines if not re.search(r'Amount:|Date:', line)]
        # Display the keys and values
        extracted_data = {}
        i = 0
        for line in filtered_lines:
            # Customize the extraction logic based on your PDF structure
            if i == 0:
                extracted_data['name'] = filtered_lines[i]
            elif i ==16:
                date_info= filtered_lines[i] + filtered_lines[i+1] + filtered_lines[i+2]
                # Find the second period (".") index
                second_period_index = date_info.find('.', date_info.find('.') + 1)
                extracted_date = date_info[second_period_index + 3:].strip()
                extracted_data['due date'] = extracted_date
            elif i == 23:
                first_space_index = filtered_lines[i].find(' ')
                second_space_index = filtered_lines[i].find(' ', first_space_index+ 1)
                extracted_amount= filtered_lines[i][first_space_index:second_space_index].strip()
                extracted_data['bill amount'] = extracted_amount
            i+=1
        # Print the extracted data
        print(f"File: {pdf_path}")
        for key, value in extracted_data.items():
            print(f"{key}: {value}")
        print("\n")
