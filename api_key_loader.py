# api_key_loader.py
"""
Module to securely load the API key from a DOCX file.
"""

from docx import Document
from config import API_KEY_FILE

def get_api_key():
    """Extract API key from a DOCX file."""
    try:
        doc = Document(API_KEY_FILE)
        return doc.paragraphs[0].text.strip()
    except Exception as e:
        raise RuntimeError(f"Error reading API key file: {e}")
