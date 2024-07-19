from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

retriever = db.as_retriever()
template = """You are helpful tweet creation assistant. Create tweet based on following context: 
{context}

Question: {question}

Helpful tweet:
"""

prompt = PromptTemplate.from_template(template)

llm = ChatOpenAI(model="gpt-4", temperature=0.9)

def format_docs(docs):
    print(docs)
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough(), }
    | prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke('Help me write tweet about chatbots and self-driving cars.')
print(result)