import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from utils import load_text_from_url, embed_text, summarize_text, text_splitter

user_url = input('Enter a valid url from which I can retrieve information for you! \n\n\n')
text = load_text_from_url(user_url)
summary = summarize_text(text)
print('\n Summary of page ...\n\n',summary, '\n\n\n')

text_str = text[0].page_content
split_text = text_splitter.split_text(text_str)

# create vectorstor from FAISS using the split text

vec_store = embed_text(split_text)

# llm
# gemini_api = "AIzaSyC9qoe-Vue-9kN7RN5HTbHD0OrVXUur6_w"
groq_api = "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"
llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api)
while (True):
    user_query = input("Seen the summary? I can expand on that. Aske me! \n\n")
    
    prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details,
        if the answer is not in the provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        Context:\n {context}?\n
        Question: \n{question}\n
    
        Answer:
        """
    prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
    docs = vec_store.similarity_search(user_query)
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    
    response = chain.invoke(
        {"input_documents": docs, "question": user_query}, return_only_outputs=True
    )
    
    print(f'\n\n {response['output_text']} \n\n')
