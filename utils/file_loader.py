import docx2txt
import PyPDF2

def load_file_text(filepath):
    if filepath.endswith(".pdf"):
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            return text
    elif filepath.endswith(".docx"):
        return docx2txt.process(filepath)
    return ""
