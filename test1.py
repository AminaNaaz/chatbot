import streamlit as st
import google.generativeai as genai
from google.generativeai.types import GenerationConfig
import PyPDF2
from docx import Document  # For reading DOCX files

# Load API Key from DOCX file
key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=key

# Load Resume from Backend (PDF)
def load_resume():
    with open("./my_resume.pdf", "rb") as file:  # Open PDF in binary mode
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

resume_text = load_resume()

# Initialize Streamlit UI
st.title("Amina's Recruitment Chatbot")
st.chat_message("assistant").write("Hello! I'm your recruitment chatbot. Ask me questions about Amina's qualifications, experience, skills, or data science!")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history first
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Take user input
user_input = st.chat_input("Ask about Amina's qualifications, experience, skills, or data science:")

if user_input:
    # Append user message first
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)  # Ensure user input is displayed first

    # Initialize Gemini Model
    model = genai.GenerativeModel("gemini-1.5-flash")
    custom_configure = GenerationConfig(max_output_tokens=1500, temperature=0.9)

    # Ensure chatbot answers resume-related queries or general data science questions
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
        "only when the user ask for conatcting me, please use the email address and linkedin and github but hide my contact number give this in bullets")

    response = model.generate_content(prompt, generation_config=custom_configure)

    # Append assistant response
    with st.chat_message("assistant"):
        st.write(response.text)
    st.session_state["messages"].append({"role": "assistant", "content": response.text})
