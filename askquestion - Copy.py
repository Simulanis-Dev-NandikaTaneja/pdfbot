import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import streamlit as st
os.environ["OPENAI_API_KEY"] = ""
embedding = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])
llm=OpenAI()

def ask_question(uuid,question):
    persist_directory = uuid
    vectordb=Chroma(persist_directory=persist_directory,embedding_function=embedding)
    qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever()
    )    
    result = qa_chain({"query": question})
    print("result: ",result["result"])
    return result["result"]
