"""
LangChain + OpenAI 快速入门示例
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# 加载 .env 文件中的环境变量
load_dotenv()


def get_llm():
    """根据环境变量创建 LLM 实例"""
    return ChatOpenAI(
        model=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
        openai_api_base=os.getenv("OPENAI_BASE_URL"),
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        temperature=os.getenv("TEMPERATURE"),
    )


def simple_chat():
    """简单的对话示例"""
    llm = get_llm()

    messages = [
        SystemMessage(content="你是一个有用的AI助手。"),
        HumanMessage(content="用一句话介绍一下 LangChain 是什么？"),
    ]

    response = llm.invoke(messages)
    print("简单对话示例:")
    print(f"回答: {response.content}")
    print("-" * 50)


def prompt_template_demo():
    """使用 Prompt Template 的示例"""
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}方面的专家。"),
            ("human", "请用简单的语言解释{topic}。"),
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "role": "编程",
            "topic": "什么是 LangChain 的 LCEL（LangChain Expression Language）",
        }
    )

    print("Prompt Template 示例:")
    print(f"回答: {response.content}")
    print("-" * 50)


def main():
    print("=" * 50)
    print("LangChain + OpenAI 教程")
    print("=" * 50)
    print()

    # 检查 API Key
    if not os.getenv("OPENAI_API_KEY"):
        print("错误: 请在 .env 文件中设置 OPENAI_API_KEY")
        print("示例: OPENAI_API_KEY=sk-your-api-key-here")
        return

    simple_chat()
    prompt_template_demo()


if __name__ == "__main__":
    main()
