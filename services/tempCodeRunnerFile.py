
import pdfplumber

def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Assume that the relevant information is in the first page
        first_page = pdf.pages[0]

        # Extract text from the first page
        text = first_page.extract_text()
        print(text)

        # Implement your logic to extract name, amount, and due date from the 'text' variable
        # For example:
        name = extract_name(text)
        amount = extract_amount(text)
        due_date = extract_due_date(text)

        return name, amount, due_date

def extract_name(text):
    # Implement logic to extract name from text
    # For example, if name is preceded by "Name:", you can do:
    start_index = text.find("Name:")
    end_index = text.find("\n", start_index)
    return text[start_index+len("Name:"):end_index].strip()

def extract_amount(text):
    # Implement logic to extract amount from text
    # For example, if amount is preceded by "Amount:", you can do:
    start_index = text.find("Amount:")
    end_index = text.find("\n", start_index)
    return text[start_index+len("Amount:"):end_index].strip()

def extract_due_date(text):
    # Implement logic to extract due date from text
    # For example, if due date is preceded by "Due Date:", you can do:
    start_index = text.find("Due Date:")
    end_index = text.find("\n", start_index)
    return text[start_index+len("Due Date:"):end_index].strip()

# Example usage
pdf_path ="0400000035201_420016942522.pdf"
name, amount, due_date = extract_data_from_pdf(pdf_path)
print("Name:", name)
print("Amount:", amount)
print("Due Date:", due_date)
