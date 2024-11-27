from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyC9qoe-Vue-9kN7RN5HTbHD0OrVXUur6_w")
answer = llm.invoke("Tell me a joke!")
print(f'{answer.content}\n')
