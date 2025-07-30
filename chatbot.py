from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model =ChatOpenAI()

while true:
    user_input =input('You: ')
    if user_input.lower =='exit':
        break
    result=model.invoke(user_input)
    print(f'Bot: {result}')