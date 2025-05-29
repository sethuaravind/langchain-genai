from langchain import hub
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_experimental.agents import create_csv_agent


def prepare_chat_model(path):
    llm = ChatOpenAI()
    embeddings = OpenAIEmbeddings()
    prompt = hub.pull('langchain-ai/retrieval-qa-chat')
    vectorstore = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

    combine_docs = create_stuff_documents_chain(llm, prompt)
    rag_llm = create_retrieval_chain(vectorstore.as_retriever(), combine_docs)

    return rag_llm


def chat_with_pdf(rag_llm, query):
    res = rag_llm.invoke({'input': query})

    return res['answer']


def chat_with_csv(path):
    llm = ChatOpenAI()
    csv_agent = create_csv_agent(llm, path, allow_dangerous_code=True)

    return csv_agent