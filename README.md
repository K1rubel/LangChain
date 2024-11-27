# LangChainTask
This is part of iCogLabs weekly intern training assignment. This one focuses on leveraging langchian package for various ends.

## File Organization
Main folder --- langChainTask -- contains the main.py file, utils and files folders
Subfolders --- 
utils -- contains all the sub-routines called in by the main.py

__init__.py -- for imports

document_loading.py -- loads text from the web using user urls makes use of *WebBaseLoader* from *langchain_community.document_loaders*

summarization.py -- produces a four-sentence summary of the whole page using *load_summarize_chain* from *langchain.chains.summarize import* and the open source LLM agent *ChatGroq* and *PromptTemplate* all from langchain module

embedding.py -- makes use of text splitter and FAISS vector store to create index for similarity search later with the user query

files -- contains sample of chain run using *https://sakana.ai/evolutionary-model-merge/* as .txt files

### Simlest application
of langchain included here as well as simplest_lang_chain.py
It surely cant get any simpler than this 😁!

### Warning
The embedder has size limitations about the number of tokens that can be handled. So take that into consideration. Apart from that and some deprecation warnings which couldnt go way despite all that I did, the system works well for custom chat based on the text from the web page.
Thanks!
