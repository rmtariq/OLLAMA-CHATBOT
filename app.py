import streamlit as st
from langchain_ollama import ChatOllama

# pip install -qU langchain-ollama
# pip install langchain

st.set_page_config(page_title="Ollama Chat Application", page_icon="🧠")

st.title("🧠 Create Your Own Chat App with Ollama and LangChain")
st.subheader("Interact with your own AI Assistant")

# Form for user input
with st.form("llm-form"):
    st.write("### Enter your question or statement:")
    text = st.text_area("Type here...", height=100, placeholder="Ask me anything!")
    submit = st.form_submit_button("Submit")

# Function to generate a response
def generate_response(input_text):
    model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")
    response = model.invoke(input_text)
    return response.content

# Store chat history in session state
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# Process the user's input and generate a response
if submit and text:
    with st.spinner("Generating response..."):
        response = generate_response(text)
        st.session_state['chat_history'].append({"user": text, "ollama": response})
        st.success("Response generated!")

# Display chat history with an expander
st.write("Starting the app...")
if submit and text:
    st.write("Processing user input...")
    with st.spinner("Generating response..."):
        response = generate_response(text)
        st.write(f"Generated response: {response}")
        st.session_state['chat_history'].append({"user": text, "ollama": response})
        st.success("Response generated!")
st.write("Finished processing input.")
