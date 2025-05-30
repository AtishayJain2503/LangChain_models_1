from langchain_openai import OpenAI
from dotenv import load_dotenv # .env file se key load karne main help karta hain


load_dotenv()

llm= OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("meri bandi kab banegi?") #communicate with the model

print(result) 