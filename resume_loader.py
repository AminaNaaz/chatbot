# resume_loader.py
"""
Module for loading and extracting text from a resume PDF.
"""

import PyPDF2
from config import RESUME_FILE

def load_resume():
    """Load and extract text from the resume PDF."""
    try:
        with open(RESUME_FILE, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except Exception as e:
        return f"Error loading resume: {e}"

resume_text = load_resume()
