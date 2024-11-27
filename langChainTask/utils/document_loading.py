# document_loading.py

from langchain_community.document_loaders import WebBaseLoader
import streamlit as st

def load_text_from_url(url):
    try:
        loader = WebBaseLoader(url)
        documents = loader.load()
        return documents
    except Exception as e:
        print('Not a valid url!')
        return None

# # print(load_text_from_url("https://sakana.ai/evolutionary-model-merge/")[0].page_content)
# text = load_text_from_url("https://sakana.ai/evolutionary-model-merge/")[0].page_content
# # write the text content to .txt file for filing purpose
# with open('/Users/bitseat/KiraFiles/iCogLabs/Training/LangChain/streamLang/files/whole_text.txt','w') as file:
#     file.write(text)