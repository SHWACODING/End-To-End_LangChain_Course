from fastapi import FastAPI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn

import os
from dotenv import load_dotenv


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.3-70b-versatile")


parser = StrOutputParser()


system_template = "Translate the following into {language}:"


prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])


chain = prompt_template | llm | parser


app = FastAPI(
    title="simpleTranslator",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)


add_routes(
    app,
    chain,
    path="/chain",
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

### http://localhost:8000/chain/playground/