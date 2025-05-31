from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv # .env file se key load karne main help karta hain


load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022', temperature=0.7, max_completion_tokens=50)


result = model.invoke("meri bandi kab banegi?") #communicate with the model

print(result.content) 