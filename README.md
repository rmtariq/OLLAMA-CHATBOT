# 🧠 Create Your Own Chat App with Ollama and LangChain

This repository contains code to create a custom chat application using [Ollama](https://ollama.com) and [LangChain](https://langchain.com). This allows you to interact with your own AI model locally using a simple web interface built with Streamlit.

## 🚀 Features
- **Interactive Chat Interface:** Ask questions and get responses from a fine-tuned LLaMA model using a web interface.
- **Local Deployment:** Run everything locally without the need for external API calls.
- **Customizable Responses:** Adjust the AI model and responses to suit your needs.

## 🛠 Prerequisites
- Python 3.8 or higher
- [Ollama installed](https://ollama.com/download)
- Basic knowledge of Python and Streamlit

## 📦 Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/rmtariq/OLLAMA-CHATBOT.git
cd OLLAMA-CHATBOT

## Step 2: Create a Virtual Environment

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

## Step 3: Install Required Packages
pip install -qU langchain-ollama streamlit

## Step 4: Pull the LLaMA Model
ollama pull llama3.2:1b

## Step 5: Start the Ollama Server
ollama serve

## Step 6: Run the Streamlit App
streamlit run app.py

## 📂 Project Structure

OLLAMA-CHATBOT/
│
├── app.py                  # Main Streamlit app
├── test_connection.py      # Test connection script
├── README.md               # This file
└── .venv/                  # Python virtual environment (not included in version control)
