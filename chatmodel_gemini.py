from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # .env file se key load karne main help karta hain


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.7, max_completion_tokens=50)
# temperature parameter controls how creative or determisnistic the response is 
# lower values mean that if we will send the prompt again and again very less change would be there but in case of higher temperature every time new output would be there for same prompt

# max_completion_token to limit the number of tokens as each token is paid 


result = model.invoke("meri bandi kab banegi?") #communicate with the model

print(result.content) 