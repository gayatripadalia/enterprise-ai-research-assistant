import fitz  # PyMuPDF
import docx
import pandas as pd


def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    return text


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def extract_text_from_excel(file_path):
    df = pd.read_excel(file_path, engine="openpyxl")
    return df.to_string(index=False)


def extract_text(file_path, file_type):
    file_type = file_type.lower()

    if file_type == "pdf":
        return extract_text_from_pdf(file_path)

    elif file_type == "docx":
        return extract_text_from_docx(file_path)

    elif file_type in ["xls", "xlsx"]:
        return extract_text_from_excel(file_path)

    else:
        return "Unsupported file type"