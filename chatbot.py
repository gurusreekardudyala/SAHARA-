import streamlit as st
from google import genai
from google.genai import types

# Configure the page
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize the Gemini client
client = genai.Client(api_key="AIzaSyBWawu0YBu6JMXmsCRexWA6-yr6JPQuDtU")

# Add a title and description
st.title("🤖 AI Chatbot")
st.markdown("""
This is an AI chatbot powered by Google's Gemini model. Ask me anything!
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt],
                config=types.GenerateContentConfig(
                    max_output_tokens=500,
                    temperature=0.7
                )
            )
            st.markdown(response.text)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})

# Add a sidebar with information
with st.sidebar:
    st.title("About")
    st.markdown("""
    This chatbot uses Google's Gemini model to generate responses.
    
    Features:
    - Interactive chat interface
    - Persistent chat history
    - Real-time responses
    
    Made with ❤️ using Streamlit
    """)