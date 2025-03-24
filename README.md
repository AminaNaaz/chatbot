## Amina's Recruitment Chatbot
This is a Streamlit-based chatbot that answers questions about Amina’s qualifications, experience, and skills using Google's Gemini API. It processes queries based on a resume (PDF) and can also provide general information on data science.

## Features
- Bullet Points Loads resume from a PDF file

- Bullet Points Uses Google's Gemini API for AI-powered responses

- Bullet Points Handles user queries related to Amina’s expertise and data science

- Bullet Points Maintains a chat history within the Streamlit session

- Bullet Points Provides professional responses while hiding personal contact details

## How It Works
1. Load Resume from a PDF
The load_resume() function reads Amina’s resume from a PDF file and extracts text using PyPDF2.

2. Initialize the Chatbot
- Bullet PointsDisplays a welcome message in Streamlit UI.

- Bullet PointsMaintains a chat history using st.session_state["messages"].

3. Process User Queries
- Bullet Points Captures user input using st.chat_input().

- Bullet Points Sends the resume and user query to Gemini API.

- Bullet Points The chatbot generates a response while ensuring:

- Bullet Points It refers to Amina’s experience in the first person (e.g., "I have experience in...").

- Bullet Points It answers general data science queries when relevant.

- Bullet Points It avoids unrelated topics politely.

- Bullet Points It shares contact details only for LinkedIn, GitHub, and email, while hiding phone numbers.

4. Display Responses
- Bullet Points The assistant's response is displayed using st.chat_message("assistant").

- Bullet Points The response is stored in st.session_state to maintain the conversation.

## Customization
- Bullet Points Update my_resume.pdf with a new resume file.

- Bullet Points Modify the prompt instructions to tweak chatbot behavior.

- Bullet Points Adjust the temperature and max_output_tokens for response control.

## Future Improvements
- Bullet Points Add support for DOCX resumes.

- Bullet Points Implement database storage for resumes and conversations.

- Bullet Points Enhance UI with Streamlit components for better interaction.

