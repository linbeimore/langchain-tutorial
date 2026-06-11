from langchain_core.prompts import PromptTemplate

# 1. 创建实例
prompt_template = PromptTemplate(
    template="请用简单的语言解释{topic}。",
    input_variables=["topic"],
)

# 2. 填充变量
prompt = prompt_template.format(topic="机器学习")

print(prompt)