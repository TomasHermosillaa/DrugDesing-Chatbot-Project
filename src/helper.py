from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load our PDFs
def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob='*.pdf',
                    loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# Create text chunks
def text_split(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap= 20) # Select the size of characters of each chunk
    text_chunks = text_splitter.split_documents(data)

    return text_chunks

# Dowload Embedding Model
def download_emb():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings