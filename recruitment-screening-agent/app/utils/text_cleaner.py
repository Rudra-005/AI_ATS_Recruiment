import re

class TextCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters except basic punctuation
        text = re.sub(r'[^\w\s\.\,\;\:\-\(\)]', '', text)
        return text.strip()
    
    @staticmethod
    def normalize_text(text: str) -> str:
        # Convert to lowercase and remove extra spaces
        text = text.lower().strip()
        text = re.sub(r'\s+', ' ', text)
        return text