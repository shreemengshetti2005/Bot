from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,systemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


chatHistory =[
    systemMessage(content="You are a helpful assistant."),
]

while True:
    user_input =input('You: ')
    chatHistory.append(HumanMessage(content=user_input))
    if user_input.lower =='exit':
        break
    result=model.invoke(user_input)
    chatHistory.append(AIMessage(content=result))
    print(f'Bot: {result}')
