# summarization.py

from langchain.chains.summarize import load_summarize_chain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

def summarize_text(text):
    prompt_template = """
    You are a text summarization tool. 
    Summarize the text in not more than four sentences. 
    Text {text}
    Out put only the summary text. 
    Do not include something like 'Here is the summary ...'
    """
    prompt = PromptTemplate.from_template(template=prompt_template)
    groq_api = "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"
    llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api)
    summarizer_chain = load_summarize_chain(llm, prompt=prompt)
    summary = summarizer_chain.invoke(text)['output_text']
    return summary


# Instances of summaries of the whole text
def append_text_to_file(file_path, text): 
    with open(file_path, "a") as file: 
        file.write(text + "\n")
# lets append three runs of the summary to summaries.txt file for reference
# for i in range(3):
#     text = document_loading.load_text_from_url('https://sakana.ai/evolutionary-model-merge/')
#     summary = summarize_text(text)
#     heading = f'Summary {i+1}\n'
#     append_text_to_file('/Users/bitseat/KiraFiles/iCogLabs/Training/LangChain/streamLang/files/summaries.txt', heading + summary)