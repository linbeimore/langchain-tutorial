# LangChain Tutorial

基于 Python + LangChain 的 AI 应用开发教程，使用 uv 进行项目管理和依赖管理。

## 功能特性

- LangChain 核心框架集成
- OpenAI API 对接（支持第三方代理）
- Prompt Template 模板化对话
- LCEL（LangChain Expression Language）链式调用

## 环境要求

- Python >= 3.12
- uv 包管理器

## 快速开始

### 1. 安装 uv

```bash
pip install uv
```

### 2. 克隆项目

```bash
git clone <repository-url>
cd langchain-tutorial
```

### 3. 安装依赖

```bash
uv sync
```

### 4. 配置环境变量

复制并编辑 `.env` 文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的 API 配置：

```env
# OpenAI API Key（必填）
OPENAI_API_KEY=sk-your-api-key-here

# API Base URL（可选，使用第三方代理时填写）
OPENAI_API_BASE=https://api.openai-proxy.com/v1

# 模型名称（根据代理支持的模型填写）
OPENAI_MODEL=gpt-3.5-turbo
```

### 5. 运行示例

```bash
uv run main.py
```

## 项目结构

```
langchain-tutorial/
├── .venv/              # Python 虚拟环境
├── .env                # 环境变量配置（不要提交到 git）
├── .gitignore          # Git 忽略配置
├── main.py             # 示例代码
├── pyproject.toml      # 项目配置和依赖
├── uv.lock             # 依赖锁定文件
└── README.md           # 项目说明
```

## 依赖说明

| 包                  | 版本    | 用途               |
| ------------------- | ------- | ------------------ |
| langchain           | >=1.3.6 | LangChain 核心框架 |
| langchain-core      | >=1.4.3 | 核心抽象和接口     |
| langchain-community | >=0.4.2 | 社区集成组件       |
| langchain-openai    | >=1.3.0 | OpenAI 集成        |
| python-dotenv       | >=1.0.0 | 环境变量管理       |

## 常用命令

```bash
# 添加新依赖
uv add <package-name>

# 添加开发依赖
uv add --dev <package-name>

# 运行 Python 脚本
uv run python <script.py>

# 激活虚拟环境（可选）
# Windows CMD
.venv\Scripts\activate.bat
# PowerShell
.venv\Scripts\Activate.ps1

# 更新依赖
uv lock --upgrade
```

## 常见问题

### 1. 模型不支持错误

如果遇到 `Not supported model` 错误，请检查 `.env` 中的 `OPENAI_MODEL` 是否为你的 API 代理支持的模型。

### 2. API Key 无效

确保 `.env` 中的 `OPENAI_API_KEY` 正确填写，且有足够的额度。

### 3. 网络连接问题

如果使用第三方代理，确保 `OPENAI_API_BASE` 地址正确且可访问。

## 示例代码说明

### simple_chat()

简单的对话示例，展示如何使用 `ChatOpenAI` 进行基本对话：

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")
messages = [
    SystemMessage(content="你是一个有用的AI助手。"),
    HumanMessage(content="用一句话介绍一下 LangChain 是什么？"),
]
response = llm.invoke(messages)
```

### prompt_template_demo()

使用 Prompt Template 的示例，展示模板化对话：

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}方面的专家。"),
    ("human", "请用简单的语言解释{topic}。"),
])

chain = prompt | llm
response = chain.invoke({"role": "编程", "topic": "什么是 LCEL"})
```

## 扩展阅读

- [LangChain 官方文档](https://python.langchain.com/)
- [LangChain OpenAI 集成](https://python.langchain.com/docs/integrations/chat/openai/)
- [LCEL 使用指南](https://python.langchain.com/docs/expression_language/)
- [uv 官方文档](https://docs.astral.sh/uv/)

## 许可证

MIT License
