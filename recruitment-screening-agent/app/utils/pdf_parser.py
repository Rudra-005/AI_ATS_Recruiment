import PyPDF2
from io import BytesIO

class PDFParser:
    @staticmethod
    def extract_text(pdf_file) -> str:
        try:
            pdf_file.seek(0)
            pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"PDF parsing error: {str(e)}")
    
    @staticmethod
    def is_valid_pdf(pdf_file) -> bool:
        try:
            pdf_file.seek(0)
            pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
            return len(pdf_reader.pages) > 0
        except:
            return False