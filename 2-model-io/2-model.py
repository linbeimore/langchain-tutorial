import os 
import dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(
    model= os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
    streaming=True,
)

messages = [
    # SystemMessage(content="你是一个助手，请回答我的问题。"),
    HumanMessage(content="你好，你是谁？"),
]

messages1 = [
    # SystemMessage(content="你是一个助手，请回答我的问题。"),
    HumanMessage(content="背诵静夜思"),
]

# # 非流式调用
# response = chat_model.invoke(messages)

# print("开始流式输出：")

# for chunk in chat_model.stream(messages): 
#     print(chunk.content, end="", flush=True) # 输出流式数据,刷新缓冲区，无换行符


# print("\n流式输出结束")


# 批量调用
response = chat_model.batch([messages, messages])
print(response)