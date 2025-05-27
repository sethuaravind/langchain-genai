from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS



def vectorize_pdf(pdf_path, name_of_vectors):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    documents = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vector_embeddings = FAISS.from_documents(documents, embeddings)
    vector_embeddings.save_local(f'Local_vectors/{name_of_vectors}')

    return True

