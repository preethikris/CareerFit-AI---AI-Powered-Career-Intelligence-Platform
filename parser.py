import PyPDF2
import pdfplumber
import docx2txt


# -------------------------------
# Extract Text from PDF
# -------------------------------

def extract_text_from_pdf(pdf_file):

    text = ""

    try:
        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                extracted_text = page.extract_text()

                if extracted_text:
                    text += extracted_text + "\n"

    except Exception as e:
        text = f"Error reading PDF: {e}"

    return text


# -------------------------------
# Extract Text from DOCX
# -------------------------------

def extract_text_from_docx(docx_file):

    try:
        text = docx2txt.process(docx_file)

    except Exception as e:
        text = f"Error reading DOCX: {e}"

    return text


# -------------------------------
# Main Resume Reader Function
# -------------------------------

def extract_resume_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):

        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):

        return extract_text_from_docx(uploaded_file)

    else:

        return "Unsupported File Format"