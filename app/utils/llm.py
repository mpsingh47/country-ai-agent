# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )


from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)