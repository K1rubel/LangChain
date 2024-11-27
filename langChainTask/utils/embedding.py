# embedding.py
import faiss
import numpy as np
from docx import Document
import logging
logging.basicConfig(level=logging.ERROR)

from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# the embedder
def embed_text(texts):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    document_search = FAISS.from_texts(texts, embeddings)
    return document_search
# Split the text using langcahins text_splitter --CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap = 200,
    length_function = len,
)
# apply the above function to split the text 
# the langchain webbasloader returns langchain_core.documents.base.Document type file
# covert it into string for furthur processing
 
# text = document_loading.load_text_from_url('https://sakana.ai/evolutionary-model-merge/')[0].page_content

# Apply the text_splitter

