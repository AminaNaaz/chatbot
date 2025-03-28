# chatbot.py
"""
Module for generating chatbot responses using Google's Gemini AI.
"""

import google.generativeai as genai
from google.generativeai.types import GenerationConfig
from api_key_loader import get_api_key
from resume_loader import resume_text
import logging
from config import LOG_FILE

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def configure_genai():
    """Configure the generative AI model with the API key."""
    try:
        genai.configure(api_key=get_api_key())
        logging.info("Chatbot API configured successfully.")
    except Exception as e:
        logging.error(f"Error configuring chatbot API: {e}")
        raise RuntimeError("Failed to configure chatbot API.")

configure_genai()

def generate_response(user_input):
    """Generate a response from the chatbot based on user input."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    custom_config = GenerationConfig(max_output_tokens=1500, temperature=0.9)

    prompt = (
    f"Amina's Resume:\n{resume_text}\n\n"
    f"User Query: {user_input}\n\n"
    "Please provide a response using 'I' when referring to skills and experience instead of mentioning the resume explicitly. "
    "If the question pertains to data science but is not covered in my experience, offer a general informative answer. "
    "For any other inquiries outside of these topics, kindly respond with: "
    "'I'm here to assist with questions related to my skillset and data science. Let me know how I can help in those areas. "
    "If you have any questions about my professional expertise, experience, or data science concepts, feel free to ask. "
    "However, I kindly refrain from discussing topics outside of these areas. Thank you for understanding.' "
    "Please maintain a professional and courteous tone throughout."
    
    "Rules for responses:"
    "- Only when the user asks for contact details, provide my email address, LinkedIn, and GitHub, but do not share my phone number. Present the details in bullet points."
    "- When the user says 'Thank you,' respond with 'You are welcome. Let me know if you need any further information.'"
    "- When the user says 'Goodbye,' respond with 'Goodbye' in a polite and professional manner."
    "- Think step by step before answering the question to ensure a clear, logical, and well-structured response."
    "- When the user says 'Hi,' respond with 'Hello' and a friendly greeting. Do not include this response when answering data science-related questions."
)


    try:
        response = model.generate_content(prompt, generation_config=custom_config)
        logging.info(f"User input: {user_input} | Response generated successfully.")
        return response.text
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "Sorry, I encountered an error. Please try again later."
