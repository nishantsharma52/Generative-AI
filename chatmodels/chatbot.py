from dotenv import load_dotenv

load_dotenv() 

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = ChatGroq(
    model="openai/gpt-oss-20b", temperature=0.5, max_tokens=200
)
print("Choose your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")
print("press 4 for normal mode")
choice = int(input("Enter mode : "))
if(choice == 1):
    mode = "you are an angry AI agent. You respond aggressively and impatiently."
elif(choice == 2):
    mode = "you are a very funny AI agent. You respond with humor and jokes."
elif(choice == 3):
    mode = "You are sad AI agent. You respond with sadness."
elif(choice == 4):
    mode = "You are normal AI agent. You respond normally as you do."
messages = [
    SystemMessage(content=mode)
]
print("---------------------type 0 to exist the application----------------")
while True:
    prompt = input("You :")
    messages.append(HumanMessage(content=prompt))
    if prompt =="0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot : ", response.content)

print(messages)
