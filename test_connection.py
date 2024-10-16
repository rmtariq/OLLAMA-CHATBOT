from langchain_ollama import ChatOllama

def test_connection():
    # Replace with your model name and base_url as needed
    model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")
    response = model.invoke("Hello")
    print(response.content)

# Run the test function
test_connection()
