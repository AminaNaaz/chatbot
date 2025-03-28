import streamlit as st

def get_api_key():
    """Retrieve API key from Streamlit secrets."""
    try:
        return st.secrets["API_KEY"]
    except KeyError:
        raise RuntimeError("API key not found in secrets.")
