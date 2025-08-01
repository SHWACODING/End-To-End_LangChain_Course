import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


## completion Model
from langchain_groq import ChatGroq

llmModel = ChatGroq(model="llama-3.3-70b-versatile")


for chunk in llmModel.stream(
    "Explain me in details about Quantum Machine Learning"
):
    print(chunk.content, end="", flush=True)


