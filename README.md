## Amina's Recruitment Chatbot
Amina’s Recruitment Chatbot is an AI-powered assistant designed to provide insights into Amina’s qualifications, experience, and skills in data science. It offers a seamless and interactive user experience through a real-time chat interface.

## Overview
This chatbot enables users to ask questions about Amina’s professional background while maintaining chat history for a smooth and engaging conversation. A welcome message is displayed once per session to enhance user experience.

The chatbot is built using Streamlit, ensuring an intuitive and user-friendly interface.

## Features
✅ Real-time AI Responses – Provides structured and informative answers.
✅ Session-Based Chat Memory – Retains conversation history for a natural experience.
✅ Interactive UI – Simple and intuitive chatbot interface.
✅ One-Time Welcome Message – Enhances usability with a personalized greeting.
✅ Secure API Key Handling – Protects sensitive credentials.

## Project Structure
main.py – The core file that runs the chatbot UI in Streamlit. It manages user interactions and chat history.

chatbot.py – Contains the logic for generating responses based on user queries.

api_key_loader.py – Handles secure retrieval of the API key from Streamlit Secrets.

.streamlit/secrets.toml – (For deployment) Stores API keys securely in Streamlit Cloud.

config.py (if applicable) – Stores configuration settings.

## How It Works
1️⃣ User enters a query in the chat interface.
2️⃣ The chatbot processes the input and generates a relevant response.
3️⃣ If an API key is required, it is securely fetched from Streamlit Secrets.
4️⃣ The chatbot displays the response, updating the chat history for continuity.

## Secure API Key Management
To keep API keys secure, they should be stored in Streamlit Secrets rather than hardcoded in the codebase.

## For Cloud Deployment
Navigate to Streamlit Cloud → Manage App → Secrets.

Add the following entry:

API_KEY = "your-secret-key"
The chatbot will automatically retrieve and use the key.

## For Local Development
Alternatively, the API key can be stored locally:

Create a .env file and add:

API_KEY=your-secret-key
Load the key in the application.

## Deployment on Streamlit Cloud
1️⃣ Push the latest version of the project to GitHub.
2️⃣ Deploy the repository using Streamlit Cloud.
3️⃣ Configure secrets to store API keys securely.

## Contributing
Contributions and feedback are welcome! Feel free to submit an issue or pull request for improvements.

## Contact
For any inquiries or collaboration opportunities, feel free to reach out me aminanaazpython@gmail.com

