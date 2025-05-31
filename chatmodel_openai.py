from langchain_openai import ChatOpenAI
from dotenv import load_dotenv # .env file se key load karne main help karta hain


load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.7, max_completion_tokens=50)

result = model.invoke("meri bandi kab banegi?") #communicate with the model

print(result.content) 