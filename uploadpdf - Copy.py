import warnings
warnings.filterwarnings("ignore")
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA

os.environ["OPENAI_API_KEY"] = ""
llm=OpenAI()

def vector(uuid,pdf):
    loaders = [
        PyPDFLoader(pdf)
    ]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1500,
        chunk_overlap = 150
    )

    splits = text_splitter.split_documents(docs)

    embedding = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])
    path = uuid
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("The new directory is created!")
    #persist_directory='C:\\Nandika\\openAIproj\\pdfans\\'+path
    persist_directory=path

    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embedding,
        persist_directory=persist_directory
    )

    print(vectordb._collection.count())

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever()
    )

    return persist_directory
