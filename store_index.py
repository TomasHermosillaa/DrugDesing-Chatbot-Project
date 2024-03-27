from src.helper import load_pdf, text_split, download_emb
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load all the variables from .env
load_dotenv()

# Read and create embedding from the PDFs
extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_emb()

# Connect with Pinecone
Pinecone(api_key=os.environ.get('PINECONE_API_KEY'),
              environment=os.environ.get('PINECONE_API_ENV'))
index_name="pdf-bot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)